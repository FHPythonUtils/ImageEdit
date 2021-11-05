"""Apply high level effects to images such as shadows and convert to black and white."""
from __future__ import annotations

from pathlib import Path

from blendmodes.blend import BlendType, blendLayers
from colourswatch.io import openColourSwatch
from layeredimage.layeredimage import LayeredImage
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from imageedit.io import getPixelDimens, getSortedColours
from imageedit.transform import findAndReplace, resize, resizeSquare

THISDIR = str(Path(__file__).resolve().parent)

# pylint:disable=unbalanced-tuple-unpacking


def roundCorners(image: Image.Image, radius: int | str) -> Image.Image:
	"""Round the corners by a number of pixels. May be preferable to use...

	roundCornersAntiAlias. Use with caution as it modifies the image param.
	radius can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (Image.Image): A PIL Image
		radius (int,str): One of pixel, percent, scale

	Returns:
		Image.Image: A PIL Image
	"""
	[radius] = getPixelDimens(image, [radius])
	circle = Image.new("RGBA", (radius * 2, radius * 2), "#00000000")
	draw = ImageDraw.Draw(circle)
	draw.ellipse((0, 0, radius * 2, radius * 2), "#ffffffff")
	alpha = Image.new("RGBA", image.size, "#ffffffff")
	background = Image.new("RGBA", image.size, "#00000000")
	w, h = image.size
	alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
	alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
	alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
	alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
	background.paste(image, (0, 0), alpha.convert("RGBA"))
	return background


def addDropShadowSimple(image: Image.Image, offset: list[int]) -> Image.Image:
	"""Add a simple drop shadow.

	Args:
		image (Image.Image): Base image to give a drop shadow
		offset (list[int, int]): Offset of the shadow as [x,y]

	Returns:
		Image.Image: A PIL Image
	"""
	border = max(abs(x) for x in offset)
	return addDropShadowComplex(image, 11, border, offset, "#ffffff00", "#00000055")


def addDropShadowComplex(
	image: Image.Image,
	iterations: int,
	border: int,
	offset: list[int],
	backgroundColour: str,
	shadowColour: str,
) -> Image.Image:
	"""From https://en.wikibooks.org/wiki/Python_Imaging_Library/Drop_Shadows.

	Args:
		image (Image.Image): Base image to give a drop shadow
		iterations (int): Number of times to apply the blur filter to the shadow
		border (int): Border to give the image to leave space for the shadow
		offset (list[int, int]): Offset of the shadow as [x,y]
		backgroundColour (str): Colour of the background
		shadowColour (str): Colour of the drop shadow

	Returns:
		Image.Image: A PIL Image
	"""
	originalSize = image.size
	# Calculate the size of the intermediate image
	fullWidth = image.size[0] + abs(offset[0]) + 2 * border
	fullHeight = image.size[1] + abs(offset[1]) + 2 * border
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
	return resize(background, originalSize[0], originalSize[1])


def roundCornersAntiAlias(image: Image.Image, radius: int) -> Image.Image:
	"""Round Corners taking a radius int as an arg and do antialias.

	Args:
		image (Image.Image): A PIL Image
		radius (int): radius in px

	Returns:
		Image.Image: Image
	"""
	factor = 2
	imageTemp = resizeSquare(image, str(factor) + "x")
	[radius] = getPixelDimens(image, [radius])
	imageTemp = roundCorners(imageTemp, radius * factor)
	return resizeSquare(imageTemp, str(1 / factor) + "x")


def convertBlackAndWhite(image: Image.Image, mode: str = "filter-darker"):
	"""Convert a PIL Image to black and white from a colour image.

	Some implementations use numpy but im not going to include the extra import

	Args:
		image (Image.Image): A PIL Image to act on
		mode (str, optional): Any of ["filter-darker", "filter-lighter",
		"background", "foreground", "edges"] Specify the mode for the function to use.
		filter-darker and lighter respectively make pixels darker than the
		average black and pixels that are lighter than the average black.
		background sets the most dominant colour to white and foreground sets
		the second most dominant color to black. edges finds the edges and sets
		them to black. non edges are white. Defaults to "filter-darker".

	Returns:
		Image.Image: The black and white image
	"""
	if mode in ["background", "foreground"]:
		image = doConvertBlackAndWhiteBGFG(image, mode)
	if mode in ["filter-darker", "filter-lighter"]:
		image = doConvertBlackAndWhiteFilter(image, mode)
	if mode == "edges":
		image = doConvertBlackAndWhiteFilter(
			image.convert("RGB").filter(ImageFilter.FIND_EDGES), "filter-lighter"
		)
	return image


def doConvertBlackAndWhiteFilter(image: Image.Image, mode: str):
	"""Low level function...

	Convert an image to black and white based on a filter: filter-darker and
	lighter respectively make pixels darker than the average black and pixels
	that are lighter than the average black.

	Args:
		image (Image.Image): A PIL Image to act on
		mode (str): filter-darker and lighter respectively make pixels darker
		than the average black and pixels that are lighter than the average black.

	Returns:
		Image.Image: The black and white image
	"""
	img = image.convert("L")
	img.thumbnail((1, 1))
	averageColour = img.getpixel((0, 0))
	# Default tp "filter-lighter"
	threshold = lambda pixel: 0 if pixel > averageColour else 255
	if mode == "filter-darker":
		threshold = lambda pixel: 0 if pixel < averageColour else 255
	converted = image.convert("L").point(threshold, mode="1")
	return converted.convert("RGBA")


def doConvertBlackAndWhiteBGFG(image, mode):
	"""Low level function...

	Convert an image to black and white based on the foreground/ background:
	background sets the most dominant colour to white and foreground sets the
	second most dominant color to black.

	Args:
		image (Image.Image): A PIL Image to act on
		mode (str): background sets the most dominant colour to white and
		foreground sets the second most dominant color to black.

	Returns:
		Image.Image: The black and white image
	"""
	if mode == "background":
		image = findAndReplace(
			image, getSortedColours(image)[0][1], (255, 255, 255, 255), (0, 0, 0, 255)
		)
	if mode == "foreground":
		image = findAndReplace(
			image, getSortedColours(image)[1][1], (0, 0, 0, 255), (255, 255, 255, 255)
		)
	return image


def addText(image: Image.Image, text: str) -> Image.Image:
	"""Add text to an image such that the resultant image is in the form...

	[img]|text. The text is in fira code and has a maximum length of 16 chars
	(text longer than this is truncated with "...")

	Args:
		image (Image.Image): A PIL Image to add text to
		text (str): A string containing text to add to the image

	Returns:
		Image.Image: Image with text
	"""
	if len(text) > 15:
		text = text[:13] + ".."
	width, height = image.size
	font = ImageFont.truetype(THISDIR + "/resources/FiraCode-Light.ttf", int(height / 2 * 0.8))
	colours = getSortedColours(image)
	backgroundColour = colours[0][1]
	foregroundColour = colours[1][1]
	background = Image.new("RGBA", (width * 5, height), backgroundColour)
	imageText = ImageDraw.Draw(background)
	imageText.text(
		(int(width * 0.9), int(height / 4)), "|" + text, font=font, fill=foregroundColour
	)
	background.paste(image.convert("RGBA"), (0, 0), image.convert("RGBA"))
	return background


def blend(
	background: Image.Image, foreground: Image.Image, blendType: BlendType, opacity: float = 1
) -> Image.Image:
	"""Blend layers using numpy array.

	Args:
		background (Image.Image): background layer
		foreground (Image.Image): foreground layer (must be same size as background)
		blendType (BlendType): The blendtype
		opacity (float): The opacity of the foreground image
	Returns:
		Image: combined image

	Specify supported blend types
	NORMAL
	MULTIPLY
	ADDITIVE
	COLOURBURN
	COLOURDODGE
	REFLECT
	GLOW
	OVERLAY
	DIFFERENCE
	NEGATION
	LIGHTEN
	DARKEN
	SCREEN
	XOR
	SOFTLIGHT
	HARDLIGHT
	GRAINEXTRACT
	GRAINMERGE
	DIVIDE
	HUE
	SATURATION
	COLOUR
	LUMINOSITY
	PINLIGHT
	VIVIDLIGHT
	EXCLUSION
	DESTIN
	DESTOUT
	DESTATOP
	SRCATOP
	"""
	# We are just aliasing the blendLayers function and making the type checker happy
	del foreground, blendType, opacity
	return background


blend = blendLayers


def applySwatch(image, swatchFile):
	"""Apply a swatch to the image using colourswatch.

	Args:
		image (Image.Image): The PIL Image
		swatchFile (string): Path to the swatch file

	Returns:
		Image: quantized image
	"""
	pal = Image.new("P", (1, 1))
	pal.putpalette(openColourSwatch(swatchFile).toPILPalette())
	rgbImage = image.convert("RGB").quantize(palette=pal, method=2, dither=0)
	background = Image.new("RGBA", image.size, "#00000000")
	background.paste(rgbImage.convert("RGBA"), (0, 0), image.convert("RGBA"))
	return background


def pixelate(image: Image.Image, pixelSize: int = 4):
	"""Apply a pixelate effect to an image. This might be used to create a retro effect.

	Args:
		image (Image.Image): A pillow image
		pixelSize (int, optional): X, Y pixels to merge. E.g. assuming image
		dimensions of 256x256 and pixelSize of 4, an image with dimensions
		256x256 will be returned with the effect of an image with size 64x64.
		Defaults to 4.

	Returns:
		Image: pixelated image
	"""
	originalSize = image.size
	width, height = int(image.size[0] / pixelSize), int(image.size[1] / pixelSize)
	downsize = image.resize((width, height), Image.NEAREST)
	return downsize.resize(originalSize, Image.NEAREST)


def removeBG(image: Image.Image):
	"""Remove the background from an image or a layeredimage.

	Args:
		image (Image.Image|layeredimage.layeredimage.LayeredImage): An image or a layered
		image

	Returns:
		Image: image without bg
	"""
	if isinstance(image, Image.Image):
		return findAndReplace(image, getSortedColours(image)[0][1], (0, 0, 0, 0))
	return LayeredImage(image.extractLayers()[1:]).getFlattenLayers()
