# effects

> Auto-generated documentation for [imageedit.effects](../../imageedit/effects.py) module.

Apply high level effects to images such as shadows and convert to black and
white

- [Imageedit](../README.md#imageedit-index) / [Modules](../README.md#imageedit-modules) / [imageedit](index.md#imageedit) / effects
    - [addDropShadowComplex](#adddropshadowcomplex)
    - [addDropShadowSimple](#adddropshadowsimple)
    - [addText](#addtext)
    - [applySwatch](#applyswatch)
    - [blend](#blend)
    - [convertBlackAndWhite](#convertblackandwhite)
    - [doConvertBlackAndWhiteBGFG](#doconvertblackandwhitebgfg)
    - [doConvertBlackAndWhiteFilter](#doconvertblackandwhitefilter)
    - [pixelate](#pixelate)
    - [removeBG](#removebg)
    - [roundCorners](#roundcorners)
    - [roundCornersAntiAlias](#roundcornersantialias)

#### Attributes

- `BlendType` - Blendtype has an assortment of effects: `bmBlendType`

## addDropShadowComplex

[[find in source code]](../../imageedit/effects.py#L57)

```python
def addDropShadowComplex(
    image,
    iterations,
    border,
    offset,
    backgroundColour,
    shadowColour,
):
```

From https://en.wikibooks.org/wiki/Python_Imaging_Library/Drop_Shadows

#### Arguments

- `image` *PIL.Image.Image* - Base image to give a drop shadow
- `iterations` *int* - Number of times to apply the blur filter to the shadow
- `border` *int* - Border to give the image to leave space for the shadow
offset ([int, int]): Offset of the shadow as [x,y]
- `backgroundColour` *string* - Colour of the background
- `shadowColour` *string* - Colour of the drop shadow

#### Returns

- `PIL.Image.Image` - A PIL Image

## addDropShadowSimple

[[find in source code]](../../imageedit/effects.py#L43)

```python
def addDropShadowSimple(image, offset):
```

#### Arguments

- `image` *PIL.Image.Image* - Base image to give a drop shadow
offset ([int, int]): Offset of the shadow as [x,y]

#### Returns

- `PIL.Image.Image` - A PIL Image

## addText

[[find in source code]](../../imageedit/effects.py#L188)

```python
def addText(image, text):
```

Add text to an image such that the resultant image is in the form
[img]|text. The text is in fira code and has a maximum length of 16 chars
(text longer than this is truncated with "...")

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image to add text to
- `text` *str* - A string containing text to add to the image

#### Returns

- `PIL.Image.Image` - Image with text

## applySwatch

[[find in source code]](../../imageedit/effects.py#L265)

```python
def applySwatch(image, swatchFile):
```

Apply a swatch to the image using colourswatch

#### Arguments

- `image` *PIL.Image.Image* - The PIL Image
- `swatchFile` *string* - Path to the swatch file

#### Returns

- `PIL.Image` - quantized image

## blend

[[find in source code]](../../imageedit/effects.py#L220)

```python
def blend(background, foreground, blendType, opacity):
```

Blend layers using numpy array

#### Arguments

- `background` *PIL.Image* - background layer
- `foreground` *PIL.Image* - foreground layer (must be same size as background)
- `blendType` *BlendType* - The blendtype
- `opacity` *float* - The opacity of the foreground image

#### Returns

- `PIL.Image` - combined image

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

## convertBlackAndWhite

[[find in source code]](../../imageedit/effects.py#L113)

```python
def convertBlackAndWhite(image, mode='filter-darker'):
```

Convert a PIL Image to black and white from a colour image. Some
implementations use numpy but im not going to include the extra import

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image to act on
- `mode` *str, optional* - Any of ["filter-darker", "filter-lighter",
"background", "foreground", "edges"] Specify the mode for the function to use.
filter-darker and lighter respectively make pixels darker than the
average black and pixels that are lighter than the average black.
background sets the most dominant colour to white and foreground sets
the second most dominant color to black. edges finds the edges and sets
them to black. non edges are white. Defaults to "filter-darker".

#### Returns

- `PIL.Image.Image` - The black and white image

## doConvertBlackAndWhiteBGFG

[[find in source code]](../../imageedit/effects.py#L165)

```python
def doConvertBlackAndWhiteBGFG(image, mode):
```

Low level
Convert an image to black and white based on the foreground/ background:
background sets the most dominant colour to white and foreground sets the
second most dominant color to black.

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image to act on
- `mode` *str* - background sets the most dominant colour to white and
foreground sets the second most dominant color to black.

#### Returns

- `PIL.Image.Image` - The black and white image

## doConvertBlackAndWhiteFilter

[[find in source code]](../../imageedit/effects.py#L140)

```python
def doConvertBlackAndWhiteFilter(image, mode):
```

Low level
Convert an image to black and white based on a filter: filter-darker and
lighter respectively make pixels darker than the average black and pixels
that are lighter than the average black.

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image to act on
- `mode` *str* - filter-darker and lighter respectively make pixels darker
than the average black and pixels that are lighter than the average black.

#### Returns

- `PIL.Image.Image` - The black and white image

## pixelate

[[find in source code]](../../imageedit/effects.py#L283)

```python
def pixelate(image, pixelSize=4):
```

Apply a pixelate effect to an image. This might be used to create a retro
effect.

#### Arguments

- `image` *PIL.Image.Image* - A pillow image
- `pixelSize` *int, optional* - X, Y pixels to merge. E.g. assuming image
dimensions of 256x256 and pixelSize of 4, an image with dimensions
256x256 will be returned with the effect of an image with size 64x64.
Defaults to 4.

#### Returns

- `PIL.Image` - pixelated image

## removeBG

[[find in source code]](../../imageedit/effects.py#L303)

```python
def removeBG(image):
```

Remove the background from an image or a layeredimage

#### Arguments

- `image` *PIL.Image.Image|layeredimage.layeredimage.LayeredImage* - An image or a layered
image

#### Returns

- `PIL.Image` - image without bg

## roundCorners

[[find in source code]](../../imageedit/effects.py#L14)

```python
def roundCorners(image, radius):
```

Round the corners by a number of pixels. May be preferable to use
roundCornersAntiAlias. Use with caution as it modifies the image param.
radius can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image
- `radius` *int|str* - One of pixel, percent, scale

#### Returns

- `PIL.Image.Image` - A PIL Image

## roundCornersAntiAlias

[[find in source code]](../../imageedit/effects.py#L96)

```python
def roundCornersAntiAlias(image, radius):
```

Round Corners taking a radius int as an arg and do antialias

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image
- `radius` *int* - radius in px

#### Returns

- `PIL.Image.Image` - Image
