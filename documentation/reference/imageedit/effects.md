# Effects

[Imageedit Index](../README.md#imageedit-index) /
[Imageedit](./index.md#imageedit) /
Effects

> Auto-generated documentation for [imageedit.effects](../../../imageedit/effects.py) module.

- [Effects](#effects)
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

## addDropShadowComplex

[Show source in effects.py:64](../../../imageedit/effects.py#L64)

From https://en.wikibooks.org/wiki/Python_Imaging_Library/Drop_Shadows.

#### Arguments

- `image` *Image.Image* - Base image to give a drop shadow
- `iterations` *int* - Number of times to apply the blur filter to the shadow
- `border` *int* - Border to give the image to leave space for the shadow
offset (list[int, int]): Offset of the shadow as [x,y]
- `backgroundColour` *str* - Colour of the background
- `shadowColour` *str* - Colour of the drop shadow

#### Returns

- `Image.Image` - A PIL Image

#### Signature

```python
def addDropShadowComplex(
    image: Image.Image,
    iterations: int,
    border: int,
    offset: list[int],
    backgroundColour: str,
    shadowColour: str,
) -> Image.Image:
    ...
```



## addDropShadowSimple

[Show source in effects.py:50](../../../imageedit/effects.py#L50)

Add a simple drop shadow.

#### Arguments

- `image` *Image.Image* - Base image to give a drop shadow
offset (list[int, int]): Offset of the shadow as [x,y]

#### Returns

- `Image.Image` - A PIL Image

#### Signature

```python
def addDropShadowSimple(image: Image.Image, offset: list[int]) -> Image.Image:
    ...
```



## addText

[Show source in effects.py:205](../../../imageedit/effects.py#L205)

Add text to an image such that the resultant image is in the form [img]|text.
The text is in fira code and has a maximum length of 16 chars
(text longer than this is truncated with "...")

#### Arguments

- `image` *Image.Image* - A PIL Image to add text to
- `text` *str* - A string containing text to add to the image

#### Returns

- `Image.Image` - Image with text

#### Signature

```python
def addText(image: Image.Image, text: str) -> Image.Image:
    ...
```



## applySwatch

[Show source in effects.py:286](../../../imageedit/effects.py#L286)

Apply a swatch to the image using colourswatch.

#### Arguments

- `image` *Image.Image* - The PIL Image
- `swatchFile` *string* - Path to the swatch file

#### Returns

- `Image` - quantized image

#### Signature

```python
def applySwatch(image, swatchFile):
    ...
```



## blend

[Show source in effects.py:233](../../../imageedit/effects.py#L233)

Blend layers using numpy array.

#### Arguments

- `background` *Image.Image* - background layer
- `foreground` *Image.Image* - foreground layer (must be same size as background)
- `blendType` *BlendType* - The blendtype
- `opacity` *float* - The opacity of the foreground image

#### Returns

- `Image` - combined image

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

#### Signature

```python
def blend(
    background: Image.Image,
    foreground: Image.Image,
    blendType: BlendType,
    opacity: float = 1,
) -> Image.Image:
    ...
```



## convertBlackAndWhite

[Show source in effects.py:124](../../../imageedit/effects.py#L124)

Convert a PIL Image to black and white from a colour image.

Some implementations use numpy but im not going to include the extra import

#### Arguments

- `image` *Image.Image* - A PIL Image to act on
- `mode` *str, optional* - Any of ["filter-darker", "filter-lighter",
"background", "foreground", "edges"] Specify the mode for the function to use.
filter-darker and lighter respectively make pixels darker than the
average black and pixels that are lighter than the average black.
background sets the most dominant colour to white and foreground sets
the second most dominant color to black. edges finds the edges and sets
them to black. non edges are white. Defaults to "filter-darker".

#### Returns

- `Image.Image` - The black and white image

#### Signature

```python
def convertBlackAndWhite(image: Image.Image, mode: str = "filter-darker"):
    ...
```



## doConvertBlackAndWhiteBGFG

[Show source in effects.py:179](../../../imageedit/effects.py#L179)

Low level function

Convert an image to black and white based on the foreground/ background:
background sets the most dominant colour to white and foreground sets the
second most dominant color to black.

#### Arguments

- `image` *Image.Image* - A PIL Image to act on
- `mode` *str* - background sets the most dominant colour to white and
foreground sets the second most dominant color to black.

#### Returns

- `Image.Image` - The black and white image

#### Signature

```python
def doConvertBlackAndWhiteBGFG(image, mode):
    ...
```



## doConvertBlackAndWhiteFilter

[Show source in effects.py:153](../../../imageedit/effects.py#L153)

Low level function

Convert an image to black and white based on a filter: filter-darker and
lighter respectively make pixels darker than the average black and pixels
that are lighter than the average black.

#### Arguments

- `image` *Image.Image* - A PIL Image to act on
- `mode` *str* - filter-darker and lighter respectively make pixels darker
than the average black and pixels that are lighter than the average black.

#### Returns

- `Image.Image` - The black and white image

#### Signature

```python
def doConvertBlackAndWhiteFilter(image: Image.Image, mode: str):
    ...
```



## pixelate

[Show source in effects.py:304](../../../imageedit/effects.py#L304)

Apply a pixelate effect to an image. This might be used to create a retro effect.

#### Arguments

- `image` *Image.Image* - A pillow image
- `pixelSize` *int, optional* - X, Y pixels to merge. E.g. assuming image
dimensions of 256x256 and pixelSize of 4, an image with dimensions
256x256 will be returned with the effect of an image with size 64x64.
Defaults to 4.

#### Returns

- `Image` - pixelated image

#### Signature

```python
def pixelate(image: Image.Image, pixelSize: int = 4):
    ...
```



## removeBG

[Show source in effects.py:323](../../../imageedit/effects.py#L323)

Remove the background from an image or a layeredimage.

#### Arguments

- `image` *Image.Image|layeredimage.layeredimage.LayeredImage* - An image or a layered
image

#### Returns

- `Image` - image without bg

#### Signature

```python
def removeBG(image: Image.Image):
    ...
```



## roundCorners

[Show source in effects.py:19](../../../imageedit/effects.py#L19)

Round the corners by a number of pixels. May be preferable to use

roundCornersAntiAlias. Use with caution as it modifies the image param.
radius can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *Image.Image* - A PIL Image
- `radius` *int,str* - One of pixel, percent, scale

#### Returns

- `Image.Image` - A PIL Image

#### Signature

```python
def roundCorners(image: Image.Image, radius: int | str) -> Image.Image:
    ...
```



## roundCornersAntiAlias

[Show source in effects.py:107](../../../imageedit/effects.py#L107)

Round Corners taking a radius int as an arg and do antialias.

#### Arguments

- `image` *Image.Image* - A PIL Image
- `radius` *int* - radius in px

#### Returns

- `Image.Image` - Image

#### Signature

```python
def roundCornersAntiAlias(image: Image.Image, radius: int) -> Image.Image:
    ...
```


