# Io

> Auto-generated documentation for [imageedit.io](../../../imageedit/io.py) module.

Author FredHappyface 2019-2022.

- [Imageedit](../README.md#imageedit-index) / [Modules](../MODULES.md#imageedit-modules) / [Imageedit](index.md#imageedit) / Io
    - [checkExists](#checkexists)
    - [combine](#combine)
    - [getImageDesc](#getimagedesc)
    - [getPixelDimens](#getpixeldimens)
    - [getSortedColours](#getsortedcolours)
    - [openImage](#openimage)
    - [openImagesInDir](#openimagesindir)
    - [reduceColours](#reducecolours)
    - [saveImage](#saveimage)

Lib containing various image editing operations

#### Attributes

- `FILE_EXTS` - fmt: off: `['bmp', 'dib', 'eps', 'gif', 'ico', 'im', 'jpeg...`

## checkExists

[[find in source code]](../../../imageedit/io.py#L177)

```python
def checkExists(file):
```

Throw an error and abort if the path does not exist.

## combine

[[find in source code]](../../../imageedit/io.py#L158)

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

## getImageDesc

[[find in source code]](../../../imageedit/io.py#L110)

```python
def getImageDesc(image: Image.Image) -> str:
```

Get an image description returns [icon/mask]. Likely more useful for my specific use case than in the general lib.

#### Arguments

- `image` *PIL.Image.Image* - Image

#### Returns

- `str` - description of image

## getPixelDimens

[[find in source code]](../../../imageedit/io.py#L30)

```python
def getPixelDimens(image: Image.Image, dimens: list[int | str]) -> list[int]:
```

Get the pixel dimensions for an image from one of the following.

pixel (no calculation): int, percent: "val%", scale: "valx"

#### Arguments

- `image` *Image.Image* - Input image
- `dimens` *int|str* - One of pixel, percent, scale

#### Returns

- `list[int]` - outDimens in pixels

## getSortedColours

[[find in source code]](../../../imageedit/io.py#L127)

```python
def getSortedColours(
    image: Image.Image,
) -> list[tuple[int, tuple[int, int, int, int]]]:
```

Get the list of colours in an image sorted by 'popularity'.

#### Arguments

- `image` *PIL.Image.Image* - Image to get colours from

#### Returns

- `(colour_count,` *colour)[]* - list of tuples in the form pixel_count, colour

## openImage

[[find in source code]](../../../imageedit/io.py#L75)

```python
def openImage(file: str, mode: str | None = None) -> Image.Image:
```

Open a single image and returns an image object.

Use full file path or file path relative to /lib

#### Arguments

- `file` *str* - full file path or file path relative to /lib
- `mode` *str,None* - open image with a mode (optional)

#### Returns

- `Image.Image` - Image

## openImagesInDir

[[find in source code]](../../../imageedit/io.py#L58)

```python
def openImagesInDir(
    dirGlob: str,
    mode: str | None = None,
) -> list[tuple[str, Image.Image]]:
```

Open all images in a directory and returns them in a list along with filepath.

#### Arguments

- `dirGlob` *str* - in the form "input/*."
- `mode` *str,None* - open image with a mode (optional)

#### Returns

- `PIL.Image.Image` - Image

## reduceColours

[[find in source code]](../../../imageedit/io.py#L143)

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

[[find in source code]](../../../imageedit/io.py#L95)

```python
def saveImage(fileName, image, optimise=True):
```

Save a single image.

Use full file path or file path relative to /lib. Pass in the image object

#### Arguments

- `fileName` *string* - full file path or file path relative to /lib
- `image` *PIL.Image.Image* - A PIL Image
- `optimise` *bool, optional* - Optimise the image?. Defaults to True.
