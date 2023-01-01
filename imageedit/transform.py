"""Apply a transformations such as crop and resize."""
from __future__ import annotations

from typing import Iterable

from PIL import Image

from imageedit.io import getPixelDimens

# pylint:disable=unbalanced-tuple-unpacking


def cropCentre(image: Image.Image, width: int | str, height: int | str) -> Image.Image:
	"""Crops the centre part of the image with a width and height.

	width, height can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (Image.Image): Input image
		width (int,str): One of pixel, percent, scale
		height (int,str): One of pixel, percent, scale

	Returns:
		Image.Image: A PIL Image
	"""
	[width, height] = getPixelDimens(image, [width, height])
	return image.crop(
		(
			int((image.width - width) / 2),
			int((image.height - height) / 2),
			int((image.width + width) / 2),
			int((image.height + height) / 2),
		)
	)


def expand(image: Image.Image, padding: int | str) -> Image.Image:
	"""Uncrops the image with a padding. padding can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (Image.Image): Input image
		padding (int,str): One of pixel, percent, scale

	Returns:
		Image.Image: A PIL Image
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


def resize(image: Image.Image, width: int | str, height: int | str) -> Image.Image:
	"""Resize an image with desired dimensions. This is most suitable for resizing non square images where a factor would not be sufficient.
	width, height can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (Image.Image): A PIL Image
		width (int,str): One of pixel, percent, scale
		height (int,str): One of pixel, percent, scale

	Returns:
		Image.Image: Image
	"""
	[width, height] = getPixelDimens(image, [width, height])
	return image.resize((width, height), Image.ANTIALIAS)


def resizeSquare(image: Image.Image, size: int | str) -> Image.Image:
	"""Resize a square image. Or make a non square image square (will stretch if input image is non-square)
	size can be one of the following:
	pixel: int, percent: "val%", scale: "valx"

	Args:
		image (Image.Image): A PIL Image
		size (int,str): One of pixel, percent, scale

	Returns:
		Image.Image: Image
	"""
	return resize(image, size, size)


def removePadding(image: Image.Image, padding: int) -> Image.Image:
	"""Take an image and preforms a centre crop and removes the padding.

	Args:
		image (Image.Image): Image
		padding (int): padding in px

	Returns:
		Image.Image: Image
	"""
	return image.crop((padding, padding, image.width - padding, image.height - padding))


def findAndReplace(
	image: Image.Image,
	find: Iterable[int],
	replace: Iterable[int],
	noMatch: Iterable[int] | None = None,
	threshold: int = 5,
) -> Image.Image:
	"""Find and replace colour in PIL Image.

	Args:
		image (Image.Image): The Image
		find ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
		replace ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
		noMatch ((r,g,b,a), optional): A tuple containing values for rgba
		from 0-255 inclusive. Set pixel colour if not matched. Default is None
		threshold (int, optional): Find and replace without an exact match.
		Default is 5

	Returns:
		Image.Image: The result
	"""

	def cmpTup(tupleA, tupleB):
		for index, _ in enumerate(tupleA):
			if (
				tupleA[index] > tupleB[index] + threshold
				or tupleA[index] < tupleB[index] - threshold
			):
				return False
		return True

	converted = image.convert("RGBA")
	pixels = converted.load()
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if cmpTup(pixels[i, j], find):
				pixels[i, j] = replace
			elif noMatch is not None:
				pixels[i, j] = noMatch

	return converted.convert("RGBA")
