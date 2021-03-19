# transform

> Auto-generated documentation for [imageedit.transform](../../imageedit/transform.py) module.

Apply a transformations such as crop and resize.

- [Imageedit](../README.md#imageedit-index) / [Modules](../README.md#imageedit-modules) / [imageedit](index.md#imageedit) / transform
    - [cropCentre](#cropcentre)
    - [expand](#expand)
    - [findAndReplace](#findandreplace)
    - [removePadding](#removepadding)
    - [resize](#resize)
    - [resizeSquare](#resizesquare)

## cropCentre

[[find in source code]](../../imageedit/transform.py#L8)

```python
def cropCentre(image: Image.Image, width, height):
```

Crops the centre part of the image with a width and height.

width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *PIL.Image.Image* - Input image
- `width` *[int|str]* - One of pixel, percent, scale
- `height` *[int|str]* - One of pixel, percent, scale

#### Returns

- `PIL.Image.Image` - A PIL Image

## expand

[[find in source code]](../../imageedit/transform.py#L33)

```python
def expand(image, padding):
```

Uncrops the image with a padding
padding can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *PIL.Image.Image* - Input image
- `padding` *[int|str]* - One of pixel, percent, scale

#### Returns

- `PIL.Image.Image` - A PIL Image

## findAndReplace

[[find in source code]](../../imageedit/transform.py#L111)

```python
def findAndReplace(image, find, replace, noMatch=None, threshold=5):
```

Find and replace colour in PIL Image

#### Arguments

- `image` *PIL.Image.Image* - The Image
- `find` *(r,g,b,a)* - A tuple containing values for rgba from 0-255 inclusive
- `replace` *(r,g,b,a)* - A tuple containing values for rgba from 0-255 inclusive
- `noMatch` *(r,g,b,a), optional* - A tuple containing values for rgba
from 0-255 inclusive. Set pixel colour if not matched. Default is None
- `threshold` *int, optional* - Find and replace without an exact match.
Default is 5

#### Returns

- `PIL.Image.Image` - The result

## removePadding

[[find in source code]](../../imageedit/transform.py#L98)

```python
def removePadding(image, padding):
```

Takes an image and preforms a centre crop and removes the padding

#### Arguments

- `image` *PIL.Image.Image* - Image
- `padding` *int* - padding in px

#### Returns

- `PIL.Image.Image` - Image

## resize

[[find in source code]](../../imageedit/transform.py#L64)

```python
def resize(image, width, height):
```

Resize an image with desired dimensions. This is most suitable for resizing non
square images where a factor would not be sufficient.
width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image
- `width` *int|str* - One of pixel, percent, scale
- `height` *int|str* - One of pixel, percent, scale

#### Returns

- `PIL.Image.Image` - Image

## resizeSquare

[[find in source code]](../../imageedit/transform.py#L82)

```python
def resizeSquare(image, size):
```

Resize a square image. Or make a non square image square (will stretch if input
image is non-square)
size can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *PIL.Image.Image* - A PIL Image
- `size` *int|str* - One of pixel, percent, scale

#### Returns

- `PIL.Image.Image` - Image
