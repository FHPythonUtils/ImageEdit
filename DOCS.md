<a name=".imageedit"></a>
## imageedit

<a name=".imageedit.effects"></a>
## imageedit.effects

Apply high level effects to images such as shadows and convert to black and
white

<a name=".imageedit.effects.roundCorners"></a>
#### roundCorners

```python
roundCorners(image, radius)
```

Round the corners by a number of pixels. May be preferable to use
roundCornersAntiAlias. Use with caution as it modifies the image param.
radius can be one of the following:
pixel: int, percent: "val%", scale: "valx"

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image
- `radius` _int|str_ - One of pixel, percent, scale
  

**Returns**:

- `PIL.Image.Image` - A PIL Image

<a name=".imageedit.effects.addDropShadowSimple"></a>
#### addDropShadowSimple

```python
addDropShadowSimple(image, offset)
```

**Arguments**:

- `image` _PIL.Image.Image_ - Base image to give a drop shadow
- `offset` _[int, int]_ - Offset of the shadow as [x,y]
  

**Returns**:

- `PIL.Image.Image` - A PIL Image

<a name=".imageedit.effects.addDropShadowComplex"></a>
#### addDropShadowComplex

```python
addDropShadowComplex(image, iterations, border, offset, backgroundColour, shadowColour)
```

From https://en.wikibooks.org/wiki/Python_Imaging_Library/Drop_Shadows

**Arguments**:

- `image` _PIL.Image.Image_ - Base image to give a drop shadow
- `iterations` _int_ - Number of times to apply the blur filter to the shadow
- `border` _int_ - Border to give the image to leave space for the shadow
- `offset` _[int, int]_ - Offset of the shadow as [x,y]
- `backgroundColour` _string_ - Colour of the background
- `shadowColour` _string_ - Colour of the drop shadow
  

**Returns**:

- `PIL.Image.Image` - A PIL Image

<a name=".imageedit.effects.roundCornersAntiAlias"></a>
#### roundCornersAntiAlias

```python
roundCornersAntiAlias(image, radius)
```

Round Corners taking a radius int as an arg and do antialias

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image
- `radius` _int_ - radius in px
  

**Returns**:

- `PIL.Image.Image` - Image

<a name=".imageedit.effects.convertBlackAndWhite"></a>
#### convertBlackAndWhite

```python
convertBlackAndWhite(image, mode="filter-darker")
```

Convert a PIL Image to black and white from a colour image. Some
implementations use numpy but im not going to include the extra import

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image to act on
- `mode` _str, optional_ - Any of ["filter-darker", "filter-lighter",
  "background", "foreground", "edges"] Specify the mode for the function to use.
  filter-darker and lighter respectively make pixels darker than the
  average black and pixels that are lighter than the average black.
  background sets the most dominant colour to white and foreground sets
  the second most dominant color to black. edges finds the edges and sets
  them to black. non edges are white. Defaults to "filter-darker".
  

**Returns**:

- `PIL.Image.Image` - The black and white image

<a name=".imageedit.effects.doConvertBlackAndWhiteFilter"></a>
#### doConvertBlackAndWhiteFilter

```python
doConvertBlackAndWhiteFilter(image, mode)
```

Low level
Convert an image to black and white based on a filter: filter-darker and
lighter respectively make pixels darker than the average black and pixels
that are lighter than the average black.

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image to act on
- `mode` _str_ - filter-darker and lighter respectively make pixels darker
  than the average black and pixels that are lighter than the average black.
  

**Returns**:

- `PIL.Image.Image` - The black and white image

<a name=".imageedit.effects.doConvertBlackAndWhiteBGFG"></a>
#### doConvertBlackAndWhiteBGFG

```python
doConvertBlackAndWhiteBGFG(image, mode)
```

Low level
Convert an image to black and white based on the foreground/ background:
background sets the most dominant colour to white and foreground sets the
second most dominant color to black.

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image to act on
- `mode` _str_ - background sets the most dominant colour to white and
  foreground sets the second most dominant color to black.
  

**Returns**:

- `PIL.Image.Image` - The black and white image

<a name=".imageedit.effects.addText"></a>
#### addText

```python
addText(image, text)
```

Add text to an image such that the resultant image is in the form
[img]|text. The text is in fira code and has a maximum length of 16 chars
(text longer than this is truncated with "...")

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image to add text to
- `text` _str_ - A string containing text to add to the image
  

**Returns**:

- `PIL.Image.Image` - Image with text

<a name=".imageedit.effects.applySwatch"></a>
#### applySwatch

```python
applySwatch(image, swatchFile)
```

Apply a swatch to the image using colourswatch

**Arguments**:

- `image` _PIL.Image.Image_ - The PIL Image
- `swatchFile` _string_ - Path to the swatch file
  

**Returns**:

- `PIL.Image` - quantized image

<a name=".imageedit.effects.pixelate"></a>
#### pixelate

```python
pixelate(image, pixelSize=4)
```

Apply a pixelate effect to an image. This might be used to create a retro
effect.

**Arguments**:

- `image` _PIL.Image.Image_ - A pillow image
- `pixelSize` _int, optional_ - X, Y pixels to merge. E.g. assuming image
  dimensions of 256x256 and pixelSize of 4, an image with dimensions
  256x256 will be returned with the effect of an image with size 64x64.
  Defaults to 4.
  

**Returns**:

- `PIL.Image` - pixelated image

<a name=".imageedit.effects.removeBG"></a>
#### removeBG

```python
removeBG(image)
```

Remove the background from an image or a layeredimage

**Arguments**:

- `image` _PIL.Image.Image|layeredimage.layeredimage.LayeredImage_ - An image or a layered
  image
  

**Returns**:

- `PIL.Image` - image without bg

<a name=".imageedit.imagegrab"></a>
## imageedit.imagegrab

Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium

<a name=".imageedit.imagegrab.doGrabWebpage"></a>
#### doGrabWebpage

```python
async doGrabWebpage(url, resolution, evalJs)
```

Go to a URL, with a browser with a set resolution and run some js
then take a screenshot

<a name=".imageedit.imagegrab.grabWebpage"></a>
#### grabWebpage

```python
grabWebpage(url, resolution=(800, 600), evalJs=None)
```

Take a screenshot of a webpage

**Arguments**:

- `url` _string_ - The url of the webpage in question
  resolution ((int,int)), optional): Set the page resolution
- `evalJs` _string_ - Javascript to run on the page
  

**Returns**:

- `PIL.Image.Image` - A PIL Image

<a name=".imageedit.imagetracer"></a>
## imageedit.imagetracer

Do a trace of an image on the filesystem using the svgtrace library

<a name=".imageedit.io"></a>
## imageedit.io

Author FredHappyface 2020
Lib containing various image editing operations

<a name=".imageedit.io.getPixelDimens"></a>
#### getPixelDimens

```python
getPixelDimens(image, dimens)
```

Get the pixel dimensions for an image from one of the following:
pixel (no calculation): int, percent: "val%", scale: "valx"

**Arguments**:

- `image` _PIL.Image.Image_ - Input image
- `dimens` _[int|str]_ - One of pixel, percent, scale
  

**Returns**:

- `int` - outDimens in pixels

<a name=".imageedit.io.openImagesInDir"></a>
#### openImagesInDir

```python
openImagesInDir(dirGlob, mode=None)
```

Opens all images in a directory and returns them in a list along with
filepath.

**Arguments**:

- `dirGlob` _string_ - in the form "input/*."
- `mode` _str|None_ - open image with a mode (optional)
  

**Returns**:

- `PIL.Image.Image` - Image

<a name=".imageedit.io.openImage"></a>
#### openImage

```python
openImage(file, mode=None)
```

Opens a single image and returns an image object.
Use full file path or file path relative to /lib

**Arguments**:

- `file` _string_ - full file path or file path relative to /lib
- `mode` _str|None_ - open image with a mode (optional)
  

**Returns**:

- `PIL.Image.Image` - Image

<a name=".imageedit.io.saveImage"></a>
#### saveImage

```python
saveImage(fileName, image, optimise=True)
```

Saves a single image.
Use full file path or file path relative to /lib. Pass in the image object

**Arguments**:

- `fileName` _string_ - full file path or file path relative to /lib
- `image` _PIL.Image.Image_ - A PIL Image
- `optimise` _bool, optional_ - Optimise the image?. Defaults to True.

<a name=".imageedit.io.getImageDesc"></a>
#### getImageDesc

```python
getImageDesc(image)
```

Gets an image description returns [icon/mask]. Likely more useful for
my specific use case than in the general lib

**Arguments**:

- `image` _PIL.Image.Image_ - Image
  

**Returns**:

- `string|none` - description of image

<a name=".imageedit.io.getSortedColours"></a>
#### getSortedColours

```python
getSortedColours(image)
```

Get the list of colours in an image sorted by 'popularity'

**Arguments**:

- `image` _PIL.Image.Image_ - Image to get colours from
  

**Returns**:

  (colour_count, colour)[]: list of tuples in the form pixel_count, colour

<a name=".imageedit.io.reduceColours"></a>
#### reduceColours

```python
reduceColours(image, mode="optimised")
```

Reduces the number of colours in an image. Modes "logo", "optimised"

**Arguments**:

- `image` _PIL.Image.Image_ - Input image
- `mode` _str, optional_ - Mode "logo" or "optimised". Defaults to
  "optimised".
  

**Returns**:

- `PIL.Image.Image` - A PIL Image

<a name=".imageedit.io.combine"></a>
#### combine

```python
combine(foregroundImage, backgroundImage, foregroundOffsets=(0, 0), backgroundOffsets=(0, 0), foregroundAlpha=1.0, backgroundAlpha=1.0)
```

Combine two images with alpha

<a name=".imageedit.io.rasterImageOA"></a>
#### rasterImageOA

```python
rasterImageOA(image, size, alpha=1.0, offsets=(0, 0))
```

Rasterise an image with offset and alpha to a given size

<a name=".imageedit.io.checkExists"></a>
#### checkExists

```python
checkExists(file)
```

Throw an error and abort if the path does not exist

<a name=".imageedit.transform"></a>
## imageedit.transform

Apply a transformations such as crop and resize

<a name=".imageedit.transform.cropCentre"></a>
#### cropCentre

```python
cropCentre(image, width, height)
```

Crops the centre part of the image with a width and height
width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

**Arguments**:

- `image` _PIL.Image.Image_ - Input image
- `width` _[int|str]_ - One of pixel, percent, scale
- `height` _[int|str]_ - One of pixel, percent, scale
  

**Returns**:

- `PIL.Image.Image` - A PIL Image

<a name=".imageedit.transform.expand"></a>
#### expand

```python
expand(image, padding)
```

Uncrops the image with a padding
padding can be one of the following:
pixel: int, percent: "val%", scale: "valx"

**Arguments**:

- `image` _PIL.Image.Image_ - Input image
- `padding` _[int|str]_ - One of pixel, percent, scale
  

**Returns**:

- `PIL.Image.Image` - A PIL Image

<a name=".imageedit.transform.resize"></a>
#### resize

```python
resize(image, width, height)
```

Resize an image with desired dimensions. This is most suitable for resizing non
square images where a factor would not be sufficient.
width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image
- `width` _int|str_ - One of pixel, percent, scale
- `height` _int|str_ - One of pixel, percent, scale
  

**Returns**:

- `PIL.Image.Image` - Image

<a name=".imageedit.transform.resizeSquare"></a>
#### resizeSquare

```python
resizeSquare(image, size)
```

Resize a square image. Or make a non square image square (will stretch if input
image is non-square)
size can be one of the following:
pixel: int, percent: "val%", scale: "valx"

**Arguments**:

- `image` _PIL.Image.Image_ - A PIL Image
- `size` _int|str_ - One of pixel, percent, scale
  

**Returns**:

- `PIL.Image.Image` - Image

<a name=".imageedit.transform.removePadding"></a>
#### removePadding

```python
removePadding(image, padding)
```

Takes an image and preforms a centre crop and removes the padding

**Arguments**:

- `image` _PIL.Image.Image_ - Image
- `padding` _int_ - padding in px
  

**Returns**:

- `PIL.Image.Image` - Image

<a name=".imageedit.transform.findAndReplace"></a>
#### findAndReplace

```python
findAndReplace(image, find, replace, noMatch=None, threshold=5)
```

Find and replace colour in PIL Image

**Arguments**:

- `image` _PIL.Image.Image_ - The Image
  find ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
  replace ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
  noMatch ((r,g,b,a), optional): A tuple containing values for rgba
  from 0-255 inclusive. Set pixel colour if not matched. Default is None
- `threshold` _int, optional_ - Find and replace without an exact match.
  Default is 5
  

**Returns**:

- `PIL.Image.Image` - The result

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

