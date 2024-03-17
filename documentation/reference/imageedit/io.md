# Io

[Imageedit Index](../README.md#imageedit-index) / [Imageedit](./index.md#imageedit) / Io

> Auto-generated documentation for [imageedit.io](../../../imageedit/io.py) module.

#### Attributes

- `FILE_EXTS` - fmt: off: ['bmp', 'dib', 'eps', 'gif', 'ico', 'im', 'jpeg', 'jpg', 'j2k', 'j2p', 'j2xjfif', 'msp', 'pcx', 'png', 'pbm', 'pgm', 'ppm', 'pnm', 'sgi', 'spi', 'tga', 'tiff', 'webp', 'xbm', 'blp', 'cur', 'dcx', 'dds', 'fli', 'flc', 'fpx', 'ftex', 'gbr', 'gd', 'imt', 'pcd', 'xpm']


- [Io](#io)
  - [checkExists](#checkexists)
  - [combine](#combine)
  - [getContrastRatio](#getcontrastratio)
  - [getImageDesc](#getimagedesc)
  - [getPixelDimens](#getpixeldimens)
  - [getSortedColours](#getsortedcolours)
  - [openImage](#openimage)
  - [openImagesInDir](#openimagesindir)
  - [reduceColours](#reducecolours)
  - [saveImage](#saveimage)

## checkExists

[Show source in io.py:207](../../../imageedit/io.py#L207)

Throw an error and abort if the path does not exist.

#### Signature

```python
def checkExists(file): ...
```



## combine

[Show source in io.py:188](../../../imageedit/io.py#L188)

Combine two images with alpha.

#### Signature

```python
def combine(
    foregroundImage,
    backgroundImage,
    foregroundOffsets=(0, 0),
    backgroundOffsets=(0, 0),
    foregroundAlpha=1.0,
    backgroundAlpha=1.0,
): ...
```



## getContrastRatio

[Show source in io.py:214](../../../imageedit/io.py#L214)

Get the contrast ratio of an image

#### Signature

```python
def getContrastRatio(image: Image.Image) -> float: ...
```



## getImageDesc

[Show source in io.py:130](../../../imageedit/io.py#L130)

Get an image description returns [icon/mask]. Likely more useful for my specific
use case than in the general lib.

#### Arguments

----
 - `image` *PIL.Image.Image* - Image

#### Returns

-------
 - `str` - description of image

#### Signature

```python
def getImageDesc(image: Image.Image) -> str: ...
```



## getPixelDimens

[Show source in io.py:40](../../../imageedit/io.py#L40)

Get the pixel dimensions for an image from one of the following.

pixel (no calculation): int, percent: "val%", scale: "valx"

#### Arguments

----
 - `image` *Image.Image* - Input image
 - `dimens` *int|str* - One of pixel, percent, scale

#### Returns

-------
 - `list[int]` - outDimens in pixels

#### Signature

```python
def getPixelDimens(image: Image.Image, dimens: list[int | str]) -> list[int]: ...
```



## getSortedColours

[Show source in io.py:151](../../../imageedit/io.py#L151)

Get the list of colours in an image sorted by 'popularity'.

#### Arguments

----
 - `image` *PIL.Image.Image* - Image to get colours from

#### Returns

-------
 - `(colour_count,` *colour)[]* - list of tuples in the form pixel_count, colour

#### Signature

```python
def getSortedColours(
    image: Image.Image,
) -> list[tuple[int, tuple[int, int, int, int]]]: ...
```



## openImage

[Show source in io.py:91](../../../imageedit/io.py#L91)

Open a single image and returns an image object.

Use full file path or file path relative to /lib

#### Arguments

----
 - `file` *str* - full file path or file path relative to /lib
 - `mode` *str,None* - open image with a mode (optional)

#### Returns

-------
 - `Image.Image` - Image

#### Signature

```python
def openImage(file: str, mode: str | None = None) -> Image.Image: ...
```



## openImagesInDir

[Show source in io.py:71](../../../imageedit/io.py#L71)

Open all images in a directory and returns them in a list along with filepath.

#### Arguments

----
 - `dirGlob` *str* - in the form "input/*."
 - `mode` *str,None* - open image with a mode (optional)

#### Returns

-------
 - `PIL.Image.Image` - Image

#### Signature

```python
def openImagesInDir(
    dirGlob: str, mode: str | None = None
) -> list[tuple[str, Image.Image]]: ...
```



## reduceColours

[Show source in io.py:170](../../../imageedit/io.py#L170)

Reduces the number of colours in an image. Modes "logo", "optimised".

#### Arguments

----
 - `image` *PIL.Image.Image* - Input image
 - `mode` *str, optional* - Mode "logo" or "optimised". Defaults to
 "optimised".

#### Returns

-------
 - `PIL.Image.Image` - A PIL Image

#### Signature

```python
def reduceColours(image: Image.Image, mode: str = "optimised"): ...
```



## saveImage

[Show source in io.py:114](../../../imageedit/io.py#L114)

Save a single image.

Use full file path or file path relative to /lib. Pass in the image object

#### Arguments

----
 - `fileName` *string* - full file path or file path relative to /lib
 - `image` *PIL.Image.Image* - A PIL Image

#### Signature

```python
def saveImage(fileName, image): ...
```