"""Author FredHappyface 2019-2022.

Lib containing various image editing operations
"""
from __future__ import annotations

import glob
import os
import sys
from pathlib import Path

from layeredimage.io import (
	LayeredImage,
	exportFlatImage,
	openLayerImage,
	saveLayerImage,
)
from layeredimage.layeredimage import renderWAlphaOffset
from PIL import Image

# fmt: off
FILE_EXTS = [
"bmp", "dib", "eps", "gif", "ico", "im", "jpeg", "jpg", "j2k", "j2p", "j2x"
"jfif", "msp", "pcx", "png", "pbm", "pgm", "ppm", "pnm", "sgi", "spi", "tga",
"tiff", "webp", "xbm", "blp", "cur", "dcx", "dds", "fli", "flc", "fpx", "ftex",
"gbr", "gd", "imt", "pcd", "xpm"]
# fmt: on


def getPixelDimens(image: Image.Image, dimens: list[int | str]) -> list[int]:
	"""Get the pixel dimensions for an image from one of the following.

	pixel (no calculation): int, percent: "val%", scale: "valx"

	Args:
		image (Image.Image): Input image
		dimens (int|str): One of pixel, percent, scale

	Returns:
		list[int]: outDimens in pixels
	"""
	outDimens = []
	for index, dimension in enumerate(dimens):
		if isinstance(dimension, int):
			outDimens.append(dimension)
		elif isinstance(dimension, str):
			if len(dimens) == 1:
				size = min(image.size)
			else:
				size = image.size[index]
			if dimension[-1] == "%":
				outDimens.append(int(size * int(dimension[:-1]) / 100))
			if dimension[-1] == "x":
				outDimens.append(int(size * float(dimension[:-1])))
	return outDimens


def openImagesInDir(dirGlob: str, mode: str | None = None) -> list[tuple[str, Image.Image]]:
	"""Open all images in a directory and returns them in a list along with filepath.

	Args:
		dirGlob (str): in the form "input/*."
		mode (str,None): open image with a mode (optional)

	Returns:
		PIL.Image.Image: Image
	"""
	images = []
	for fileExt in FILE_EXTS:
		for file in glob.glob(dirGlob + "." + fileExt):
			images.append((file, openImage(file, mode)))
	return images


def openImage(file: str, mode: str | None = None) -> Image.Image:
	"""Open a single image and returns an image object.

	Use full file path or file path relative to /lib

	Args:
		file (str): full file path or file path relative to /lib
		mode (str,None): open image with a mode (optional)

	Returns:
		Image.Image: Image
	"""
	checkExists(file)
	if mode is not None:
		image = reduceColours(Image.open(file), mode)
	else:
		image = Image.open(file)
	return image


def saveImage(fileName, image, optimise=True):
	"""Save a single image.

	Use full file path or file path relative to /lib. Pass in the image object

	Args:
		fileName (string): full file path or file path relative to /lib
		image (PIL.Image.Image): A PIL Image
		optimise (bool, optional): Optimise the image?. Defaults to True.
	"""
	os.makedirs(Path(fileName).parent, exist_ok=True)
	image = reduceColours(image) if optimise else image
	image.save(fileName, optimize=optimise, quality=75)


def getImageDesc(image: Image.Image) -> str:
	"""Get an image description returns [icon/mask]. Likely more useful for my specific use case than in the general lib.

	Args:
		image (PIL.Image.Image): Image

	Returns:
		str: description of image
	"""
	desc = "unknown"
	if image.width == 640 and image.height == 640:
		desc = "mask"
	elif image.width == 512 and image.height == 512:
		desc = "icon"
	return desc


def getSortedColours(
	image: Image.Image,
) -> list[tuple[int, tuple[int, int, int, int]]]:
	"""Get the list of colours in an image sorted by 'popularity'.

	Args:
		image (PIL.Image.Image): Image to get colours from

	Returns:
		(colour_count, colour)[]: list of tuples in the form pixel_count, colour
	"""
	rgbaImage = image.convert("RGBA")
	colors = rgbaImage.getcolors(maxcolors=256**3)
	return sorted(colors, key=lambda item: item[0], reverse=True)


def reduceColours(image: Image.Image, mode: str = "optimised"):
	"""Reduces the number of colours in an image. Modes "logo", "optimised".

	Args:
		image (PIL.Image.Image): Input image
		mode (str, optional): Mode "logo" or "optimised". Defaults to
		"optimised".

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	modes = {"logo": 16, "optimised": 256}
	return image.quantize(colors=modes[mode.lower()], method=2, kmeans=1, dither=None)


def combine(
	foregroundImage,
	backgroundImage,
	foregroundOffsets=(0, 0),
	backgroundOffsets=(0, 0),
	foregroundAlpha=1.0,
	backgroundAlpha=1.0,
):
	"""Combine two images with alpha."""
	maxSize = (
		max(backgroundImage.size[0], foregroundImage.size[0]),
		max(backgroundImage.size[1], foregroundImage.size[1]),
	)
	return Image.alpha_composite(
		renderWAlphaOffset(backgroundImage, maxSize, backgroundAlpha, backgroundOffsets),
		renderWAlphaOffset(foregroundImage, maxSize, foregroundAlpha, foregroundOffsets),
	)


def checkExists(file):
	"""Throw an error and abort if the path does not exist."""
	if not os.path.exists(file):
		print(f"ERROR: {file} does not exist")
		sys.exit(1)
