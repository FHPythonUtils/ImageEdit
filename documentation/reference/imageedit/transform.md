# Transform

[Imageedit Index](../README.md#imageedit-index) /
[Imageedit](./index.md#imageedit) /
Transform

> Auto-generated documentation for [imageedit.transform](../../../imageedit/transform.py) module.

- [Transform](#transform)
  - [cropCentre](#cropcentre)
  - [expand](#expand)
  - [findAndReplace](#findandreplace)
  - [removePadding](#removepadding)
  - [resize](#resize)
  - [resizeSquare](#resizesquare)

## cropCentre

[Show source in transform.py:13](../../../imageedit/transform.py#L13)

Crops the centre part of the image with a width and height.

width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *Image.Image* - Input image
- `width` *int,str* - One of pixel, percent, scale
- `height` *int,str* - One of pixel, percent, scale

#### Returns

- `Image.Image` - A PIL Image

#### Signature

```python
def cropCentre(
    image: Image.Image, width: int | str, height: int | str
) -> Image.Image: ...
```



## expand

[Show source in transform.py:38](../../../imageedit/transform.py#L38)

Uncrops the image with a padding. padding can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *Image.Image* - Input image
- `padding` *int,str* - One of pixel, percent, scale

#### Returns

- `Image.Image` - A PIL Image

#### Signature

```python
def expand(image: Image.Image, padding: int | str) -> Image.Image: ...
```



## findAndReplace

[Show source in transform.py:115](../../../imageedit/transform.py#L115)

Find and replace colour in PIL Image.

#### Arguments

- `image` *Image.Image* - The Image
- `find` *(r,g,b,a)* - A tuple containing values for rgba from 0-255 inclusive
- `replace` *(r,g,b,a)* - A tuple containing values for rgba from 0-255 inclusive
- `noMatch` *(r,g,b,a), optional* - A tuple containing values for rgba
from 0-255 inclusive. Set pixel colour if not matched. Default is None
- `threshold` *int, optional* - Find and replace without an exact match.
Default is 5

#### Returns

- `Image.Image` - The result

#### Signature

```python
def findAndReplace(
    image: Image.Image,
    find: Iterable[int],
    replace: Iterable[int],
    noMatch: Iterable[int] | None = None,
    threshold: int = 5,
) -> Image.Image: ...
```



## removePadding

[Show source in transform.py:102](../../../imageedit/transform.py#L102)

Take an image and preforms a centre crop and removes the padding.

#### Arguments

- `image` *Image.Image* - Image
- `padding` *int* - padding in px

#### Returns

- `Image.Image` - Image

#### Signature

```python
def removePadding(image: Image.Image, padding: int) -> Image.Image: ...
```



## resize

[Show source in transform.py:68](../../../imageedit/transform.py#L68)

Resize an image with desired dimensions. This is most suitable for resizing non
square images where a factor would not be sufficient.
width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *Image.Image* - A PIL Image
- `width` *int,str* - One of pixel, percent, scale
- `height` *int,str* - One of pixel, percent, scale

#### Returns

- `Image.Image` - Image

#### Signature

```python
def resize(image: Image.Image, width: int | str, height: int | str) -> Image.Image: ...
```



## resizeSquare

[Show source in transform.py:86](../../../imageedit/transform.py#L86)

Resize a square image. Or make a non square image square (will stretch if
input image is non-square)
size can be one of the following:
pixel: int, percent: "val%", scale: "valx"

#### Arguments

- `image` *Image.Image* - A PIL Image
- `size` *int,str* - One of pixel, percent, scale

#### Returns

- `Image.Image` - Image

#### Signature

```python
def resizeSquare(image: Image.Image, size: int | str) -> Image.Image: ...
```