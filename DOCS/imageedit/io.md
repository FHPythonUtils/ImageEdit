# io

> Auto-generated documentation for [imageedit.io](../../imageedit/io.py) module.

Author FredHappyface 2020.

- [Imageedit](../README.md#imageedit-index) / [Modules](../README.md#imageedit-modules) / [imageedit](index.md#imageedit) / io
    - [checkExists](#checkexists)
    - [combine](#combine)
    - [exportFlatImage](#exportflatimage)
    - [getImageDesc](#getimagedesc)
    - [getPixelDimens](#getpixeldimens)
    - [getSortedColours](#getsortedcolours)
    - [openImage](#openimage)
    - [openImagesInDir](#openimagesindir)
    - [openLayerImage](#openlayerimage)
    - [rasterImageOA](#rasterimageoa)
    - [reduceColours](#reducecolours)
    - [saveImage](#saveimage)
    - [saveLayerImage](#savelayerimage)

Lib containing various image editing operations

#### Attributes

- `FILE_EXTS` - fmt: off: `['bmp', 'dib', 'eps', 'gif', 'ico', 'im', 'jpeg...`

## checkExists

[[find in source code]](../../imageedit/io.py#L205)

```python
def checkExists(file):
```

Throw an error and abort if the path does not exist.

## combine

[[find in source code]](../../imageedit/io.py#L179)

```python
def combine(
    foregroundImage,
    backgroundImage,
    foregroundOffsets=(0, 0),
    backgroundOffsets=(0, 0),
    foregroundAlpha=1.0,
    backgroundAlpha=1.0,
):
```

Combine two images with alpha.

## exportFlatImage

[[find in source code]](../../imageedit/io.py#L122)

```python
def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None:
```

Export to a flat image.

## getImageDesc

[[find in source code]](../../imageedit/io.py#L129)

```python
def getImageDesc(image: Image.Image):
```

Get an image description returns [icon/mask]. Likely more useful for...

my specific use case than in the general lib.

#### Arguments

- `image` *PIL.Image.Image* - Image

#### Returns

- `string|none` - description of image

## getPixelDimens

[[find in source code]](../../imageedit/io.py#L28)

```python
def getPixelDimens(image, dimens):
```

Get the pixel dimensions for an image from one of the following.

pixel (no calculation): int, percent: "val%", scale: "valx"

#### Arguments

- `image` *PIL.Image.Image* - Input image
- `dimens` *int|str* - One of pixel, percent, scale

#### Returns

- `int` - outDimens in pixels

## getSortedColours

[[find in source code]](../../imageedit/io.py#L148)

```python
def getSortedColours(
    image: Image.Image,
) -> list[tuple[(int, tuple[(int, int, int, int)])]] | list[tuple[(int, int)]]:
```

Get the list of colours in an image sorted by 'popularity'.

#### Arguments

- `image` *PIL.Image.Image* - Image to get colours from

#### Returns

- `(colour_count,` *colour)[]* - list of tuples in the form pixel_count, colour

## openImage

[[find in source code]](../../imageedit/io.py#L73)

```python
def openImage(file, mode=None):
```

Open a single image and returns an image object.

Use full file path or file path relative to /lib

#### Arguments

- `file` *string* - full file path or file path relative to /lib
- `mode` *str|None* - open image with a mode (optional)

#### Returns

- `PIL.Image.Image` - Image

## openImagesInDir

[[find in source code]](../../imageedit/io.py#L56)

```python
def openImagesInDir(dirGlob, mode=None):
```

Open all images in a directory and returns them in a list along with filepath.

#### Arguments

- `dirGlob` *string* - in the form "input/*."
- `mode` *str|None* - open image with a mode (optional)

#### Returns

- `PIL.Image.Image` - Image

## openLayerImage

[[find in source code]](../../imageedit/io.py#L93)

```python
def openLayerImage(file: str) -> LayeredImage:
```

Open a layered image.

## rasterImageOA

[[find in source code]](../../imageedit/io.py#L198)

```python
def rasterImageOA(image, size, alpha=1.0, offsets=(0, 0)):
```

Rasterise an image with offset and alpha to a given size.

## reduceColours

[[find in source code]](../../imageedit/io.py#L164)

```python
def reduceColours(image: Image.Image, mode: str = 'optimised'):
```

Reduces the number of colours in an image. Modes "logo", "optimised".

#### Arguments

- `image` *PIL.Image.Image* - Input image
- `mode` *str, optional* - Mode "logo" or "optimised". Defaults to
"optimised".

#### Returns

- `PIL.Image.Image` - A PIL Image

## saveImage

[[find in source code]](../../imageedit/io.py#L100)

```python
def saveImage(fileName, image, optimise=True):
```

Save a single image.

Use full file path or file path relative to /lib. Pass in the image object

#### Arguments

- `fileName` *string* - full file path or file path relative to /lib
- `image` *PIL.Image.Image* - A PIL Image
- `optimise` *bool, optional* - Optimise the image?. Defaults to True.

## saveLayerImage

[[find in source code]](../../imageedit/io.py#L115)

```python
def saveLayerImage(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image.
