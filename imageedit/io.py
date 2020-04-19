'''
Author FredHappyface 2020
Lib containing various image editing operations
'''
import glob
import os
import sys
from pathlib import Path
from PIL import Image
from metprint import LogType, Logger, FHFormatter

FILE_EXTS = [
"bmp", "dib", "eps", "gif", "ico", "im", "jpeg", "jpg", "j2k", "j2p", "j2x"
"jfif", "msp", "pcx", "png", "pbm", "pgm", "ppm", "pnm", "sgi", "spi", "tga", "tiff", "webp",
"xbm", "blp", "cur", "dcx", "dds", "fli", "flc", "fpx", "ftex", "gbr", "gd", "imt", "pcd", "xpm"]


class Layer:
	""" A representation of an image layer """
	def __init__(self, image, name, dimensions, offsets=(0, 0), opacity=1.0, visible=True):
		self.image = image
		self.name = name
		self.offsets = offsets
		self.opacity = opacity
		self.visible = visible
		self.dimensions = dimensions


class LayeredImage:
	""" A representation of a layered image such as an ora """
	def __init__(self, layers, dimensions):
		self.layers = layers
		self.dimensions = dimensions

	def addLayerRaster(self, image, name, offsets=(0, 0)):
		""" Raster an image and add as a layer """
		layer = rasterImageOA(image, self.dimensions, alpha=1.0, offsets=offsets)
		self.addLayer(Layer(layer, name, self.dimensions))

	def insertLayerRaster(self, image, name, index, offsets=(0, 0)):
		""" Raster an image and insert the layer """
		layer = rasterImageOA(image, self.dimensions, alpha=1.0, offsets=offsets)
		self.insertLayer(Layer(layer, name, self.dimensions), index)

	def getLayer(self, index):
		""" Get a layer """
		return self.layers[index]

	def addLayer(self, layer):
		""" Add a layer """
		self.layers.append(layer)

	def insertLayer(self, layer, index):
		""" Insert a layer at a specific index """
		self.layers.insert(index, layer)

	def removeLayer(self, index):
		""" Remove a layer at a specific index """
		self.layers.pop(index)

	def getFlattenLayers(self, ignoreHidden=True):
		""" Return an image for all flattened layers """
		if not ignoreHidden and self.layers[0].visible:
			flattenedSoFar = Image.new("RGBA", self.dimensions)
		else:
			flattenedSoFar = rasterImageOA(self.layers[0].image, self.dimensions,
			self.layers[0].opacity, self.layers[0].offsets)
		for layer in range(1, len(self.layers)):
			if not ignoreHidden and self.layers[layer].visible:
				foregroundRaster = Image.new("RGBA", self.dimensions)
			else:
				foregroundRaster = rasterImageOA(self.layers[layer].image, self.dimensions,
				self.layers[layer].opacity, self.layers[layer].offsets)
			flattenedSoFar = Image.alpha_composite(flattenedSoFar, foregroundRaster)
		return flattenedSoFar

	def getFlattenTwoLayers(self, background, foreground, ignoreHidden=True):
		""" Return an image for two flattened layers """
		if not ignoreHidden and self.layers[background].visible:
			backgroundRaster = Image.new("RGBA", self.dimensions)
		else:
			backgroundRaster = rasterImageOA(self.layers[background].image, self.dimensions,
			self.layers[background].opacity, self.layers[background].offsets)
		if not ignoreHidden and self.layers[background].visible:
			foregroundRaster = Image.new("RGBA", self.dimensions)
		else:
			foregroundRaster = rasterImageOA(self.layers[foreground].image, self.dimensions,
			self.layers[foreground].opacity, self.layers[foreground].offsets)
		return Image.alpha_composite(backgroundRaster, foregroundRaster)

	def flattenTwoLayers(self, background, foreground, ignoreHidden=True):
		""" Flatten two layers """
		image = self.getFlattenTwoLayers(background, foreground, ignoreHidden)
		self.removeLayer(foreground)
		self.layers[background] = Layer(image,
		self.layers[background].name + " (flattened)", self.dimensions)

	def flattenLayers(self, ignoreHidden=True):
		""" Flatten all layers """
		image = self.getFlattenLayers(ignoreHidden)
		self.layers[0] = Layer(image,
		self.layers[0].name + " (flattened)", self.dimensions)
		for layer in range(1, len(self.layers)):
			self.removeLayer(layer)


def getPixelDimens(image, dimens):
	"""Get the pixel dimensions for an image from one of the following:
	pixel (no calculation): int, percent: "val%", scale: "valx"

	Args:
		image (PIL.Image.Image): Input image
		dimens ([int|str]): One of pixel, percent, scale

	Returns:
		int: outDimens in pixels
	"""
	outDimens = []
	for index, dimension in enumerate(dimens):
		if isinstance(dimension, int):
			outDimens.append(dimension)
		if isinstance(dimension, str):
			if len(dimens) == 1:
				size = min(image.size)
			else:
				size = image.size[index]
			if dimension[-1] == "%":
				outDimens.append(int(size * int(dimension[:-1]) / 100))
			if dimension[-1] == "x":
				outDimens.append(int(size * float(dimension[:-1])))
	return outDimens


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
	checkExists(file)
	if mode is not None:
		image = reduceColours(Image.open(file), mode)
	else:
		image = Image.open(file)
	return image


def openLayerImage(file, mode=None):
	""" Open a layered image """
	checkExists(file)
	if ".ora" in file:
		from pyora import Project, TYPE_LAYER
		layers = []
		project = Project.load(file)
		for layer in project.iter_layers:
			if mode is not None:
				image = reduceColours(layer.get_image_data(True), mode)
			else:
				image = layer.get_image_data(True)
			layers.append(
			Layer(image, layer.name, layer.dimensions, layer.offsets, layer.opacity,
			layer.visible))
		return LayeredImage(layers, project.dimensions)

	if ".psd" in file:
		from psd_tools import PSDImage
		layers = []
		project = PSDImage.load(file)
		for layer in project.layers[::-1]:
			if mode is not None:
				image = reduceColours(layer.as_PIL(), mode)
			else:
				image = layer.as_PIL()
			layers.append(
			Layer(image, layer.name, (layer.width, layer.height), (layer.left, layer.top),
			layer.opacity / 255, layer.visible))
		return LayeredImage(layers, (project.width, project.height))
	return LayeredImage([], (0, 0))



def saveImage(fileName, image, optimise=True):
	"""Saves a single image.
	Use full file path or file path relative to /lib. Pass in the image object

	Args:
		fileName (string): full file path or file path relative to /lib
		image (PIL.Image.Image): A PIL Image
		optimise (bool, optional): Optimise the image?. Defaults to True.
	"""
	os.makedirs(Path(fileName).parent, exist_ok=True)
	if optimise:
		image = reduceColours(image)
	image.save(fileName, optimize=optimise, quality=75)


def saveLayerImage(fileName, layeredImage):
	""" Save a layered image """
	from pyora import Project
	project = Project.new(layeredImage.dimensions[0], layeredImage.dimensions[1])
	for layer in layeredImage.layers:
		project.add_layer(layer.image,
		layer.name,
		offsets=(int(layer.offsets[0] / 2), int(layer.offsets[1] / 2)),
		opacity=layer.opacity,
		visible=layer.visible)
	project.save(fileName)


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


def reduceColours(image, mode="optimised"):
	"""Reduces the number of colours in an image. Modes "logo", "optimised"

	Args:
		image (PIL.Image.Image): Input image
		mode (str, optional): Mode "logo" or "optimised". Defaults to
		"optimised".

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	modes = {"logo": 16, "optimised": 256}
	return image.quantize(colors=modes[mode.lower()], method=2, kmeans=1, dither=None)


def combine(foregroundImage,
backgroundImage,
foregroundOffsets=(0, 0),
backgroundOffsets=(0, 0),
foregroundAlpha=1.0,
backgroundAlpha=1.0):
	""" Combine two images with alpha """
	maxSize = (max(backgroundImage.size[0],
	foregroundImage.size[0]), max(backgroundImage.size[1], foregroundImage.size[1]))
	return Image.alpha_composite(
	rasterImageOA(backgroundImage, maxSize, backgroundAlpha, backgroundOffsets),
	rasterImageOA(foregroundImage, maxSize, foregroundAlpha, foregroundOffsets))


def rasterImageOA(image, size, alpha=1.0, offsets=(0, 0)):
	""" Rasterise an image with offset and alpha to a given size"""
	imageOffset = Image.new("RGBA", size)
	imageOffset.paste(image.convert("RGBA"), offsets, image.convert("RGBA"))
	return Image.blend(Image.new("RGBA", size), imageOffset, alpha)


def checkExists(file):
	""" Throw an error and abort if the path does not exist """
	if not os.path.exists(file):
		Logger(FHFormatter()).logPrint(file + " does not exist", LogType.ERROR)
		sys.exit(1)
