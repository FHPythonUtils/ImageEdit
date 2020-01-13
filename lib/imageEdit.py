'''
Author FredHappyface 20190930

Lib containing various image editing operations
'''

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import glob
import re
import os
import inspect
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
FILE_EXTS = ["png", "jpg"]


def logPrint(printText, printType="standard"):
	"""Print in the style of metasploit ("[*] infomation"). printType
	"standard", "success", "warning", "error", "info"

	Args:
		printText (str): Text to print
		printType (str, optional): How to print. Defaults to "standard".
	"""
	types = {"standard": "{}", "success": "[\033[92m+ Success\033[00m] {}",
	"warning": "[\033[93m/ Warning\033[00m] {}", "error": "[\033[91m- Error\033[00m] {}",
	"info": "[\033[96m* Info\033[00m] {}", "bold": "\033[01m{}\033[00m"}
	print(types[printType.lower()] .format(printText))


def reduceColours(image, mode="optimised"):
	"""Reduces the number of colours in an image. Modes "logo", "optimised"

	Args:
		image (PIL.Image.Image): Input image
		mode (str, optional): Mode "logo" or "optimised". Defaults to
		"optimised".

	Returns:
		PIL.Image.Image: A PIl Image
	"""
	modes = {"logo": 16, "optimised": 256}
	return image.quantize(colors=modes[mode.lower()], method=2, kmeans=1, dither=None)


def cropCentre(image, width, height):
	"""Crops the centre part of the image with a width and height
	width, height can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (PIL.Image.Image): Input image
		width ([int|str]): One of pixel, percent, scale
		height ([int|str]): One of pixel, percent, scale

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	[width, height] = getPixelDimens(image, [width, height])
	return image.crop(((image.width - width) / 2, (image.height - height) / 2,
	(image.width + width) / 2, (image.height + height) / 2))


def uncrop(image, padding):
	"""Uncrops the image with a padding
	padding can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (PIL.Image.Image): Input image
		padding ([int|str]): One of pixel, percent, scale

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	[padding] = getPixelDimens(image, [padding])
	fullWidth = image.size[0] + 2 * padding
	fullHeight = image.size[1] + 2 * padding
	background = Image.new("RGBA", (fullWidth, fullHeight))
	# Corners
	background.paste(image.convert("RGBA"))
	background.paste(image.convert("RGBA"), (2 * padding, 0))
	background.paste(image.convert("RGBA"), (0, 2 * padding))
	background.paste(image.convert("RGBA"), (2 * padding, 2 * padding))
	# Edges
	background.paste(image.convert("RGBA"), (0, padding))
	background.paste(image.convert("RGBA"), (2 * padding, padding))
	background.paste(image.convert("RGBA"), (padding, 0))
	background.paste(image.convert("RGBA"), (padding, 2 * padding))
	# Centre
	background.paste(image.convert("RGBA"), (padding, padding))
	return background


def getPixelDimens(image, dimens):
	"""Get the pixel dimensions for an image from one of the following:
	pixel (no calculation): int, percent: "val%", scale: "valx"

	Args:
		image (PIL.Image.Image): Input image
		dimens ([int|str]): One of pixel, percent, scale
	Returns:
		[int]: outDimens in pixels
	"""
	outDimens = []
	for index, dimen in enumerate(dimens):
		if isinstance(dimen, int):
			outDimens.append(dimen)
		if isinstance(dimen, str):
			if len(dimens) == 1:
				size = min(image.size)
			else:
				size = image.size[index]
			if dimen[-1] == "%":
				outDimens.append(int(size * int(dimen[:-1]) / 100))
			if dimen[-1] == "x":
				outDimens.append(int(size * float(dimen[:-1])))
	return outDimens


def roundCorners(image, radius):
	"""Round the corners by a number of pixels. May be preferable to use
	roundCornersAntiAlias. Use with caution as it modifies the image param.
	radius can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Function by fraxel: https://stackoverflow.com/users/1175101/fraxel
	https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi

	Args:
		image (PIL.Image.Image): A PIL Image
		radius (int|str): One of pixel, percent, scale

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	[radius] = getPixelDimens(image, [radius])
	circle = Image.new('RGBA', (radius * 2, radius * 2), "#00000000")
	draw = ImageDraw.Draw(circle)
	draw.ellipse((0, 0, radius * 2, radius * 2), "#ffffffff")
	alpha = Image.new('RGBA', image.size, "#ffffffff")
	background = Image.new('RGBA', image.size, "#00000000")
	w, h = image.size
	alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
	alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
	alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
	alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
	background.paste(image, (0, 0), alpha.convert("RGBA"))
	return background


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
	fullWidth = image.size[0] + abs(offset[0]) + 2 *border
	fullHeight = image.size[1] + abs(offset[1]) + 2 *border

	# Create the shadow's image. Match the parent image's mode.
	background = Image.new("RGBA", (fullWidth, fullHeight), backgroundColour)
	shadow = Image.new("RGBA", (originalSize[0], originalSize[1]), shadowColour)

	# Place the shadow, with the required offset
	shadowLeft = border + max(offset[0], 0)
	shadowTop = border + max(offset[1], 0)
	# Paste in the constant colour
	background.paste(shadow.convert("RGBA"), (shadowLeft, shadowTop), image.convert("RGBA"))

	# Apply the BLUR filter repeatedly
	for _ in range(iterations):
		background = background.filter(ImageFilter.BLUR)

	# Paste the original image on top of the shadow
	imgLeft = border - min(offset[0], 0)
	imgTop = border - min(offset[1], 0)
	background.paste(image.convert("RGBA"), (imgLeft, imgTop), image.convert("RGBA"))

	return resizeImage(background, originalSize[0], originalSize[1])


def resizeImage(image, width, height):
	"""Resize an image with desired dimensions. This is most suitable for resizing non
	square images where a factor would not be sufficient.
	width, height can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (PIL.Image.Image): A PIL Image
		width (int|str): One of pixel, percent, scale
		height (int|str): One of pixel, percent, scale

	Returns:
		PIL.Image.Image: Image
	"""
	[width, height] = getPixelDimens(image, [width, height])
	return image.resize((width, height), Image.ANTIALIAS)


def resizeImageSquare(image, size):
	"""Resize a square image. Or make a non square image square (will stretch if input
	image is non-square)
	size can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (PIL.Image.Image): A PIL Image
		size (int|str): One of pixel, percent, scale

	Returns:
		PIL.Image.Image: Image
	"""
	return resizeImage(image, size, size)


def roundCornersAntiAlias(image, radius):
	"""Round Corners taking a radius int as an arg and do antialias

	Args:
		image (PIL.Image.Image): A PIL Image
		radius (int): radius in px

	Returns:
		PIL.Image.Image: Image
	"""
	FACTOR = 2
	imageTemp = resizeImageSquare(image, str(FACTOR) +"x")
	[radius] = getPixelDimens(image, [radius])
	imageTemp = roundCorners(imageTemp, radius * FACTOR)
	return resizeImageSquare(imageTemp, str(1 /FACTOR)+"x")


def openImagesInDir(dirGlob, mode=None):
	"""Opens all images in a directory and returns them in a list along with
	filepath.

	Args:
		dirGlob (string): in the form "input/*."
		mode (str|None): open image with a mode (optional)

	Returns:
		PIL.Image.Image: Image
	"""
	images = []
	for fileExt in FILE_EXTS:
		for file in glob.glob(dirGlob + "." + fileExt):
			images.append((file, openImage(file, mode)))
	return images


def openImage(file, mode=None):
	"""Opens a single image and returns an image object.
	Use full file path or file path relative to /lib

	Args:
		file (string): full file path or file path relative to /lib
		mode (str|None): open image with a mode (optional)

	Returns:
		PIL.Image.Image: Image
	"""
	if mode is not None:
		image = reduceColours(Image.open(file), mode)
	else:
		image = Image.open(file)
	return image


def saveImage(fileName, image, optimise=True):
	"""Saves a single image.
	Use full file path or file path relative to /lib. Pass in the image object

	Args:
		fileName (string): full file path or file path relative to /lib
		image (PIL.Image.Image): A PIL Image
		optimise (bool, optional): Optimise the image?. Defaults to True.
	"""
	createDirsIfRequired(fileName)
	if optimise:
		image = reduceColours(image)
	image.save(fileName, optimize=optimise, quality=75)


def createDirsIfRequired(filepath):
	"""Create directories if required when writing a file

	Args:
		filepath (string): full file path or file path relative to /lib
	"""
	tok = re.split(os.sep, filepath)
	checkfile = ''
	for x in tok[:-1]:
		checkfile += x + os.sep
	os.makedirs(checkfile, exist_ok=True)


def removeImagePadding(image, padding):
	"""Takes an image and preforms a centre crop and removes the padding

	Args:
		image (PIL.Image.Image): Image
		padding (int): padding in px

	Returns:
		PIL.Image.Image: Image
	"""
	return image.crop((padding, padding, image.width - padding, image.height - padding))


def getImageDesc(image):
	"""Gets an image description returns [icon/mask]. Likely more useful for
	my specific use case than in the general lib

	Args:
		image (PIL.Image.Image): Image

	Returns:
		string|none: description of image
	"""
	desc = "unknown"
	if (image.width == 640 and image.height == 640):
		desc = "mask"
	elif (image.width == 512 and image.height == 512):
		desc = "icon"
	return desc


def convertBlackAndWhite(image, mode="filter-darker"):
	"""Convert a PIL Image to black and white from a colour image. Some
	implementations use numpy but im not going to include the extra import

	Args:
		image (PIL.Image.Image): A PIL Image to act on
		mode (str, optional): Any of ["filter-darker", "filter-lighter",
		"background", "foreground", "edges"] Specify the mode for the function to use.
		filter-darker and lighter respectively make pixels darker than the
		average black and pixels that are lighter than the average black.
		background sets the most dominant colour to white and foreground sets
		the second most dominant color to black. edges finds the edges and sets
		them to black. non edges are white. Defaults to "filter-darker".

	Returns:
		PIL.Image.Image: The black and white image
	"""
	if (mode in ["background", "foreground"]):
		image = doConvertBlackAndWhiteBGFG(image, mode)
	if (mode in ["filter-darker", "filter-lighter"]):
		image = doConvertBlackAndWhiteFilter(image, mode)
	if (mode == "edges"):
		image = doConvertBlackAndWhiteFilter(image.convert("RGB").filter(
			ImageFilter.FIND_EDGES), "filter-lighter")
	return image


def doConvertBlackAndWhiteFilter(image, mode):
	"""Low level
	Convert an image to black and white based on a filter: filter-darker and
	lighter respectively make pixels darker than the average black and pixels
	that are lighter than the average black.

	Args:
		image (PIL.Image.Image): A PIL Image to act on
		mode (str): filter-darker and lighter respectively make pixels darker
		than the average black and pixels that are lighter than the average black.

	Returns:
		PIL.Image.Image: The black and white image
	"""
	im = image.convert('L')
	im.thumbnail((1, 1))
	averageColour = im.getpixel((0, 0))

	if (mode == "filter-darker"):
		threshold = lambda pixel: 0 if pixel < averageColour else 255
	if (mode == "filter-lighter"):
		threshold = lambda pixel: 0 if pixel > averageColour else 255

	converted = image.convert('L').point(threshold, mode='1')
	return converted.convert("RGBA")


def doConvertBlackAndWhiteBGFG(image, mode):
	"""Low level
	Convert an image to black and white based on the foreground/ background:
	background sets the most dominant colour to white and foreground sets the
	second most dominant color to black.

	Args:
		image (PIL.Image.Image): A PIL Image to act on
		mode (str): background sets the most dominant colour to white and
		foreground sets the second most dominant color to black.

	Returns:
		PIL.Image.Image: The black and white image
	"""
	if (mode == "background"):
		image = findAndReplace(image, getSortedColours(image)[0][1], (255, 255, 255, 255), (0, 0, 0, 255))
	if (mode == "foreground"):
		image = findAndReplace(image, getSortedColours(image)[1][1], (0, 0, 0, 255), (255, 255, 255, 255))
	return image


def getSortedColours(image):
	"""Get the list of colours in an image sorted by 'popularity'

	Args:
		image (PIL.Image.Image): Image to get colours from

	Returns:
		(colour_count, colour)[]: list of tuples in the form pixel_count, colour
	"""
	rgbaImage = image.convert('RGBA')
	colors = rgbaImage.getcolors()

	def getKey(item):
		return item[0]

	if colors is not None:
		sortedColours = sorted(colors, key=getKey, reverse=True)
	else:
		sortedColours = [(1, (255, 255, 255, 255)), (1, (1, 1, 1, 255))]
	return sortedColours


def addText(image, text):
	"""Add text to an image such that the resultant image is in the form
	[img]|text. The text is in fira code and has a maximum length of 16 chars
	(text longer than this is truncated with "...")

	Args:
		image (PIL.Image.Image): A PIL Image to add text to
		text (str): A string containing text to add to the image

	Returns:
		PIL.Image.Image: Image with text
	"""
	if len(text) > 15:
		text = text[:13] + ".."
	width, height = image.size
	font = ImageFont.truetype(THISDIR + "/FiraCode-Light.ttf", int(height /2 * 0.8))
	colours = getSortedColours(image)
	backgroundColour = colours[0][1]
	foregroundColour = colours[1][1]
	background = Image.new("RGBA", (width * 5, height), backgroundColour)
	imageText = ImageDraw.Draw(background)
	imageText.text((int(width * 0.9), int(height /4)), "|" +text, font=font, fill=foregroundColour)
	background.paste(image.convert("RGBA"), (0, 0), image.convert("RGBA"))
	return background


def findAndReplace(image, find, replace, noMatch=None):
	"""Find and replace colour in PIL Image

	Args:
		image (PIL.Image.Image): The Image
		find ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
		replace ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
		noMatch ((r,g,b,a) default=None): A tuple containing values for rgba
		from 0-255 inclusive. Optional, set pixel colour if not matched

	Returns:
		PIL.Image.Image: The result
	"""
	def cmpTup(tupleA, tupleB):
		for index, _ in enumerate(tupleA):
			if (tupleA[index] > tupleB[index] + 10 or tupleA[index] < tupleB[index] - 10):
				return False
		return True

	converted = image.convert('RGBA')
	pixels = converted.load()
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if cmpTup(pixels[i, j], find):
				pixels[i, j] = replace
			elif noMatch is not None:
				pixels[i, j] = noMatch

	return converted.convert("RGBA")
