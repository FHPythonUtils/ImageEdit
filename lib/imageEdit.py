'''
Author FredHappyface 20190930

Lib containing various image editing operations
'''

from PIL import Image, ImageDraw, ImageFilter
import glob
import re
import os

FILE_EXTS = ["png", "jpg"]


def roundCornersPercent(image, radius):
	"""Round image corners by a percent. May be preferable to use
	roundCornersPercentAntiAlias

	Arguments:
		image {PIL.Image.Image} -- An image object
		radius {int} -- A radius in pixels

	Returns:
		PIL.Image.Image -- An image object
	"""
	w, h = image.size
	size = min([w, h])
	rad = int(size*radius/100)
	return roundCorners(image, rad)


def roundCorners(image, radius):
	"""Round the corners by a number of pixels. May be preferable to use
	roundCornersAntiAlias. Use with caution as it modifies the image param

	Function by fraxel: https://stackoverflow.com/users/1175101/fraxel
	https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi

	Args:
		image (PIL.Image.Image): A PIL Image
		radius (int): A radius in pixels

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	circle = Image.new('L', (radius * 2, radius * 2), 0)
	draw = ImageDraw.Draw(circle)
	draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
	alpha = Image.new('L', image.size, 255)
	w, h = image.size
	alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
	alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
	alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
	alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
	image.putalpha(alpha)
	return image


def addDropShadowSimple(image, offset):
	"""

	Args:
		image (PIL.Image.Image): Base image to give a drop shadow
		offset ([int, int]): Offset of the shadow as [x,y]

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	border = max(map(abs, offset))
	return addDropShadowComplex(image, 11, border, offset, "#ffffff00", "#00000055")

def addDropShadowComplex(image, iterations, border, offset, backgroundColour, shadowColour):
	"""From https://en.wikibooks.org/wiki/Python_Imaging_Library/Drop_Shadows

	Args:
		image (PIL.Image.Image): Base image to give a drop shadow
		iterations (int): Number of times to apply the blur filter to the shadow
		border (int): Border to give the image to leave space for the shadow
		offset ([int, int]): Offset of the shadow as [x,y]
		backgroundColour (string): Colour of the background
		shadowColour (string): Colour of the drop shadow

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	originalSize = image.size

	# Calculate the size of the intermediate image
	fullWidth = image.size[0] + abs(offset[0]) + 2*border
	fullHeight = image.size[1] + abs(offset[1]) + 2*border

	# Create the shadow's image. Match the parent image's mode.
	shadow = Image.new("RGBA", (fullWidth, fullHeight), backgroundColour)

	# Place the shadow, with the required offset
	shadowLeft = border + max(offset[0], 0)
	shadowTop = border + max(offset[1], 0)
	# Paste in the constant colour
	shadow.paste(shadowColour,
				[shadowLeft, shadowTop,
				 shadowLeft + image.size[0],
				 shadowTop  + image.size[1]], image)

	# Apply the BLUR filter repeatedly
	for _ in range(iterations):
		shadow = shadow.filter(ImageFilter.BLUR)

	# Paste the original image on top of the shadow
	imgLeft = border - min(offset[0], 0)
	imgTop = border - min(offset[1], 0)
	shadow.paste(image, (imgLeft, imgTop), image)

	return resizeImageAbs(shadow, originalSize[0], originalSize[1])


def resizeImageAbs(image, width, height):
	"""Resize an image with desired dimensions. This is most suitable for resizing non
	square images where a factor would not be sufficient

	Args:
		image (PIL.Image.Image): A PIL Image
		width (int): width in px
		height (int): height in px

	Returns:
		PIL.Image.Image: Image
	"""
	return image.resize((width, height), Image.ANTIALIAS)



def resizeImageSquare(image, size):
	"""Resize a square image. Or make a non square image square (will stretch if input
	image is non-square)

	Args:
		image (PIL.Image.Image): A PIL Image
		size (int): width and height in px

	Returns:
		PIL.Image.Image: Image
	"""
	return resizeImageAbs(image, size, size)



def resizeImage(image, factor):
	"""Resize an image by a factor. eg 2 will double the image dimensions, 0.5 would
	halve them

	Args:
		image (PIL.Image.Image): A PIL Image
		factor (int): a factor where 2 is double the dimensions, and 0.5 is half

	Returns:
		PIL.Image.Image: Image
	"""
	return resizeImageAbs(image, int(image.width*factor), int(image.height*factor))



def roundCornersAntiAlias(image, radius):
	"""Round Corners taking a radius int as an arg and do antialias

	Args:
		image (PIL.Image.Image): A PIL Image
		radius (int): radius in px

	Returns:
		PIL.Image.Image: Image
	"""
	FACTOR = 2
	imageTemp = resizeImage(image, FACTOR)
	imageTemp = roundCorners(imageTemp, radius * FACTOR)
	return resizeImage(imageTemp, 1/FACTOR)



def roundCornersPercentAntiAlias(image, radius):
	"""Round Corners taking a Percentage int as an arg (eg. 50 > 50%) and do
	antialias

	Args:
		image (PIL.Image.Image): A PIL Image
		radius (int): int as a percentage. eg 50 = 50%

	Returns:
		PIL.Image.Image: Image
	"""
	FACTOR = 2
	imageTemp = resizeImage(image, FACTOR)
	imageTemp = roundCornersPercent(imageTemp, radius * FACTOR)
	return resizeImage(imageTemp, 1/FACTOR)



def openImagesInDir(dirGlob):
	"""Opens all images in a directory and returns them in a list along with
	filepath.

	Args:
		dirGlob (string): in the form "input/*."

	Returns:
		PIL.Image.Image: Image
	"""
	images = []
	for fileExt in FILE_EXTS:
		for file in glob.glob(dirGlob + "." + fileExt):
			images.append((file, Image.open(file)))
	return images



def openImage(file):
	"""Opens a single image and returns an image object.
	Use full file path or file path relative to /lib

	Args:
		file (string): full file path or file path relative to /lib

	Returns:
		PIL.Image.Image: Image
	"""
	return Image.open(file)


def saveImage(fileName, image, optimise=True):
	"""Saves a single image.
	Use full file path or file path relative to /lib. Pass in the image object

	Args:
		fileName (string): full file path or file path relative to /lib
		image (PIL.Image.Image): A PIL Image
		optimise (bool, optional): OPtimise the image?. Defaults to True.
	"""
	createDirsIfRequired(fileName)
	if optimise:
		image = image.convert('P', palette=Image.ADAPTIVE, colors=255)
	image.save(fileName, optimize=optimise, quality=75)


def createDirsIfRequired(filepath):
	"""Create directories if required when writing a file

	Args:
		filepath (string): full file path or file path relative to /lib
	"""
	tok = re.split('/|\\\\', filepath)
	checkfile = ''
	for x in tok[:-1]:
		checkfile += x + '\\'
	os.makedirs(checkfile, exist_ok=True)


def removeImagePadding(image, padding):
	"""Takes an image and preforms a centre crop and removes the padding

	Args:
		image (PIL.Image.Image): Image
		padding (int): padding in px

	Returns:
		PIL.Image.Image: Image
	"""
	return image.crop((padding, padding, image.width -padding, image.height -padding))


def getImageDesc(image):
	"""Gets an image description returns [icon/mask]. Likely more useful for
	my specific use case than in the general lib

	Args:
		image (PIL.Image.Image): Image

	Returns:
		string|none: description of image
	"""
	if (image.width == 640 and image.height == 640):
		return "mask"
	elif (image.width == 512 and image.height == 512):
		return "icon"
