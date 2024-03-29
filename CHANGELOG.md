# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2023 - 2023/01/08

- Add tox config
- Use playwright and install_playwright in-place of pyppeteer

## 2022.0.2 - 2022/05/02

- Code quality improvements

## 2022.0.1 - 2022/04/06

- Remove metprint
- Move docs

## 2022 - 2022/01/23

- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Update deps

## 2021.0.2 - 2021/11/05

- pre-commit
- code quality improvements
- reformat files

## 2021 - 2021/03/18

- Update Pillow >= 8.1.1 due to high severity security vulnerabilities:
	- CVE-2021-27923
	- CVE-2020-35654
	- CVE-2020-35653
	- CVE-2021-27921
	- CVE-2021-27922
	- CVE-2020-35655

## 2020.5 - 2020/05/18

- Updated tests
- Added `applySwatch`, `pixelate` and `removeBG` to `effects.py`
- Added `exportFlatImage` to `io.py`

## 2020.4.2 - 2020/05/06

- Updated classifiers
- Added blendmodes
- Use svgtrace to do the imagetracing
- Use layeredimage to deal with more layered image formats such as xcf
- Added make.py

## 2020.4.1 - 2020/04/19

- First use of my updated cal versioning 😱  🎉
- Bugfixes: offset should now behave (tests seem OK, see readWriteLayered.py)
flatten functions write a layer and no longer an image 😌

## 2020.4 - 2020/04/19

- Basic layered image support

```python
class Layer:
	""" A representation of an image layer """
	def __init__(self, image, name, offsets, opacity, visible, dimensions):
		self.image = image
		self.name = name
		self.offsets = offsets # Doesn't look to be required
		self.opacity = opacity
		self.visible = visible
		self.dimensions = dimensions

class LayeredImage:
	""" A representation of a layered image such as an ora """
	def __init__(self, layers, dimensions):
		self.layers = layers
		self.dimensions = dimensions
	def addLayerRaster(self, image, name, offsets=(0, 0)):
		""" The recommended way to add a layer """

	def insertLayerRaster(self, image, name, index, offsets=(0, 0)):
		""" The recommended way to insert a layer """

	def getLayer(self, index):
		""" Get a layer """

	def addLayer(self, layer):
		""" Add a layer """

	def insertLayer(self, layer, index):
		""" Insert a layer at a specific index """

	def removeLayer(self, index):
		""" Remove a layer at a specific index """

	def getFlattenLayers(self, ignoreHidden=True):
		""" Return an image for all flattened layers """

	def getFlattenTwoLayers(self, background, foreground, ignoreHidden=True):
		""" Return an image for two flattened layers """

	def flattenTwoLayers(self, background, foreground, ignoreHidden=True):
		""" Flatten two layers """

	def flattenLayers(self, ignoreHidden=True):
		""" Flatten all layers """
```

To modify a layer you would need to do something like:

```python
# Grab the PIL Image from a layer and do stuff
layer = layeredImage.getLayer(1).image
crop = imageedit.transform.cropCentre(layer, 100, 100)
# Remove the old layer 1 and raster the new layer 1
layeredImage.removeLayer(1)
layeredImage.insertLayerRaster(crop, "Cropped Layer @1", 1, offsets=(50, 0))
```

- Using poetry and dephell
- Other significant refactoring (I guess this shows a limitation of calendar
versioning)

## 2020.3 - 2020/03/16

- Release to pypi.org. Rename library files

## 2020.2 - 2020/01/27

- Removed function **createDirsIfRequired** from imageEdit.py and replaced with
	a one-liner that does the same thing

## 2020.1 - 2020/01/22

- Removed imageTrace.py as it was slow and I honestly don't see why anyone
	would use it over imageTracerJs.py
- Added imageGrab.py
- Added Docs.md for library documentation
- Updated README
- Tidied up libraries and scripts

## Add New functions to imageEdit.py - 2020/01/13

```python
logPrint(printText, printType="standard"):
reduceColours(image, mode="optimised"):
cropCentre(image, width, height):
uncrop(image, padding):
getPixelDimens(image, dimens):
```

## Add Changelog (overdue) - 2020/01/13

- Add a changelog to the project that is rather overdue
- Lib consists of the following files:
	- FiraCode-Light.ttf
	- imageEdit.py
	- imageTrace.py
	- imagetracer.html
	- imagetracer.js
	- imageTracerJs.py
