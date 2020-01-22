# Libs

## imageEdit

Author FredHappyface 2020
Lib containing various image editing operations

### logPrint
```python
logPrint(printText, printType='standard')
```
Print in the style of metasploit ("[*] infomation"). printType
"standard", "success", "warning", "error", "info"

Args:
 printText (str): Text to print
 printType (str, optional): How to print. Defaults to "standard".

### reduceColours
```python
reduceColours(image, mode='optimised')
```
Reduces the number of colours in an image. Modes "logo", "optimised"

Args:
 image (PIL.Image.Image): Input image
 mode (str, optional): Mode "logo" or "optimised". Defaults to
 "optimised".

Returns:
 PIL.Image.Image: A PIl Image

### cropCentre
```python
cropCentre(image, width, height)
```
Crops the centre part of the image with a width and height
width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

Args:
 image (PIL.Image.Image): Input image
 width ([int|str]): One of pixel, percent, scale
 height ([int|str]): One of pixel, percent, scale

Returns:
 PIL.Image.Image: A PIL Image

### uncrop
```python
uncrop(image, padding)
```
Uncrops the image with a padding
padding can be one of the following:
pixel: int, percent: "val%", scale: "valx"

Args:
 image (PIL.Image.Image): Input image
 padding ([int|str]): One of pixel, percent, scale

Returns:
 PIL.Image.Image: A PIL Image

### getPixelDimens
```python
getPixelDimens(image, dimens)
```
Get the pixel dimensions for an image from one of the following:
pixel (no calculation): int, percent: "val%", scale: "valx"

Args:
 image (PIL.Image.Image): Input image
 dimens ([int|str]): One of pixel, percent, scale
Returns:
 [int]: outDimens in pixels

### roundCorners
```python
roundCorners(image, radius)
```
Round the corners by a number of pixels. May be preferable to use
roundCornersAntiAlias. Use with caution as it modifies the image param.
radius can be one of the following:
pixel: int, percent: "val%", scale: "valx"

Function by fraxel: https://stackoverflow.com/users/1175101/fraxel
https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi

Args:
 image (PIL.Image.Image): A PIL Image
 radius (int|str): One of pixel, percent, scale

Returns:
 PIL.Image.Image: A PIL Image

### addDropShadowSimple
```python
addDropShadowSimple(image, offset)
```

Args:
 image (PIL.Image.Image): Base image to give a drop shadow
 offset ([int, int]): Offset of the shadow as [x,y]

Returns:
 PIL.Image.Image: A PIL Image

### addDropShadowComplex
```python
addDropShadowComplex(image, iterations, border, offset, backgroundColour, shadowColour)
```
From https://en.wikibooks.org/wiki/Python_Imaging_Library/Drop_Shadows

Args:
 image (PIL.Image.Image): Base image to give a drop shadow
 iterations (int): Number of times to apply the blur filter to the shadow
 border (int): Border to give the image to leave space for the shadow
 offset ([int, int]): Offset of the shadow as [x,y]
 backgroundColour (string): Colour of the background
 shadowColour (string): Colour of the drop shadow

Returns:
 PIL.Image.Image: A PIL Image

### resizeImage
```python
resizeImage(image, width, height)
```
Resize an image with desired dimensions. This is most suitable for resizing non
square images where a factor would not be sufficient.
width, height can be one of the following:
pixel: int, percent: "val%", scale: "valx"

Args:
 image (PIL.Image.Image): A PIL Image
 width (int|str): One of pixel, percent, scale
 height (int|str): One of pixel, percent, scale

Returns:
 PIL.Image.Image: Image

### resizeImageSquare
```python
resizeImageSquare(image, size)
```
Resize a square image. Or make a non square image square (will stretch if input
image is non-square)
size can be one of the following:
pixel: int, percent: "val%", scale: "valx"

Args:
 image (PIL.Image.Image): A PIL Image
 size (int|str): One of pixel, percent, scale

Returns:
 PIL.Image.Image: Image

### roundCornersAntiAlias
```python
roundCornersAntiAlias(image, radius)
```
Round Corners taking a radius int as an arg and do antialias

Args:
 image (PIL.Image.Image): A PIL Image
 radius (int): radius in px

Returns:
 PIL.Image.Image: Image

### openImagesInDir
```python
openImagesInDir(dirGlob, mode=None)
```
Opens all images in a directory and returns them in a list along with
filepath.

Args:
 dirGlob (string): in the form "input/*."
 mode (str|None): open image with a mode (optional)

Returns:
 PIL.Image.Image: Image

### openImage
```python
openImage(file, mode=None)
```
Opens a single image and returns an image object.
Use full file path or file path relative to /lib

Args:
 file (string): full file path or file path relative to /lib
 mode (str|None): open image with a mode (optional)

Returns:
 PIL.Image.Image: Image

### saveImage
```python
saveImage(fileName, image, optimise=True)
```
Saves a single image.
Use full file path or file path relative to /lib. Pass in the image object

Args:
 fileName (string): full file path or file path relative to /lib
 image (PIL.Image.Image): A PIL Image
 optimise (bool, optional): Optimise the image?. Defaults to True.

### createDirsIfRequired
```python
createDirsIfRequired(filepath)
```
Create directories if required when writing a file

Args:
 filepath (string): full file path or file path relative to /lib

### removeImagePadding
```python
removeImagePadding(image, padding)
```
Takes an image and preforms a centre crop and removes the padding

Args:
 image (PIL.Image.Image): Image
 padding (int): padding in px

Returns:
 PIL.Image.Image: Image

### getImageDesc
```python
getImageDesc(image)
```
Gets an image description returns [icon/mask]. Likely more useful for
my specific use case than in the general lib

Args:
 image (PIL.Image.Image): Image

Returns:
 string|none: description of image

### convertBlackAndWhite
```python
convertBlackAndWhite(image, mode='filter-darker')
```
Convert a PIL Image to black and white from a colour image. Some
implementations use numpy but im not going to include the extra import

Args:
 image (PIL.Image.Image): A PIL Image to act on
 mode (str, optional): Any of ["filter-darker", "filter-lighter",
 "background", "foreground", "edges"] Specify the mode for the function to use.
 filter-darker and lighter respectively make pixels darker than the
 average black and pixels that are lighter than the average black.
 background sets the most dominant colour to white and foreground sets
 the second most dominant color to black. edges finds the edges and sets
 them to black. non edges are white. Defaults to "filter-darker".

Returns:
 PIL.Image.Image: The black and white image

### doConvertBlackAndWhiteFilter
```python
doConvertBlackAndWhiteFilter(image, mode)
```
Low level
Convert an image to black and white based on a filter: filter-darker and
lighter respectively make pixels darker than the average black and pixels
that are lighter than the average black.

Args:
 image (PIL.Image.Image): A PIL Image to act on
 mode (str): filter-darker and lighter respectively make pixels darker
 than the average black and pixels that are lighter than the average black.

Returns:
 PIL.Image.Image: The black and white image

### doConvertBlackAndWhiteBGFG
```python
doConvertBlackAndWhiteBGFG(image, mode)
```
Low level
Convert an image to black and white based on the foreground/ background:
background sets the most dominant colour to white and foreground sets the
second most dominant color to black.

Args:
 image (PIL.Image.Image): A PIL Image to act on
 mode (str): background sets the most dominant colour to white and
 foreground sets the second most dominant color to black.

Returns:
 PIL.Image.Image: The black and white image

### getSortedColours
```python
getSortedColours(image)
```
Get the list of colours in an image sorted by 'popularity'

Args:
 image (PIL.Image.Image): Image to get colours from

Returns:
 (colour_count, colour)[]: list of tuples in the form pixel_count, colour

### addText
```python
addText(image, text)
```
Add text to an image such that the resultant image is in the form
[img]|text. The text is in fira code and has a maximum length of 16 chars
(text longer than this is truncated with "...")

Args:
 image (PIL.Image.Image): A PIL Image to add text to
 text (str): A string containing text to add to the image

Returns:
 PIL.Image.Image: Image with text

### findAndReplace
```python
findAndReplace(image, find, replace, noMatch=None)
```
Find and replace colour in PIL Image

Args:
 image (PIL.Image.Image): The Image
 find ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
 replace ((r,g,b,a)): A tuple containing values for rgba from 0-255 inclusive
 noMatch ((r,g,b,a) default=None): A tuple containing values for rgba
 from 0-255 inclusive. Optional, set pixel colour if not matched

Returns:
 PIL.Image.Image: The result

## imageGrab

Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium

### grabWebpage
```python
grabWebpage(url, resolution=(800, 600))
```
Take a screenshot of a webpage

Args:
 url (string): The url of the webpage in question
 resolution ((int,int)), optional): Set the page resolution
Returns:
 PIL.Image.Image: A PIL Image

## imageTracerJs

Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium
Requires imagetracer.html and imagetracer.js along with the modules below

### doTrace
```python
doTrace(filename, mode='default')
```
Main method to call web code

### trace
```python
trace(filename, blackAndWhite=False, mode='default')
```
Do a trace of an image on the filesystem using the pyppeteer library

Args:
 filename (string): The location of the file on the filesystem, use an
 absolute filepath for this
 blackAndWhite (bool, optional): Trace a black and white SVG. Defaults to False.
 mode (str, optional): Set the mode. See https://github.com/jankovicsandras/imagetracerjs
 for more information. Defaults to "default".

Returns:
 str: SVG string
