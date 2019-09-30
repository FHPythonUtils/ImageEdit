'''
Author FredHappyface 20190930

Lib containing various image editing operations
'''

from PIL import Image, ImageDraw, ImageFilter
import glob

FILE_EXTS = ["png", "jpg"]

'''
Round image corners by a percent. May be preferable to use
roundCornersPercentAntiAlias
'''
def roundCornersPercent(image, radius):
    w, h = image.size
    size = min([w,h])
    rad = int(size*radius/100)
    return roundCorners(image, rad)


'''
Round the corners by a number of pixels. May be preferable to use
roundCornersAntiAlias. Use with caution as it modifies the image param

Function by fraxel: https://stackoverflow.com/users/1175101/fraxel
https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi
'''
def roundCorners(image, radius):
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    alpha = Image.new('L', image.size, 255)
    w, h = image.size
    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
    image.putalpha(alpha)
    return image


'''
image: base image to give a drop shadow
offset: offset of the shadow as [x,y]
'''
def addDropShadowSimple(image, offset):
    border = max(map(abs, offset))
    return addDropShadowComplex(image, 11, border, offset, "#ffffff00", "#00000055")

'''
image: base image to give a drop shadow
iterations: number of times to apply the blur filter to the shadow
border: border to give the image to leave space for the shadow
offset: offset of the shadow as [x,y]
backgroundColour: colour of the background
shadowColour: colour of the drop shadow

from https://en.wikibooks.org/wiki/Python_Imaging_Library/Drop_Shadows
'''
def addDropShadowComplex(image, iterations, border, offset, backgroundColour, shadowColour):
    originalSize = image.size

    #Calculate the size of the intermediate image
    fullWidth  = image.size[0] + abs(offset[0]) + 2*border
    fullHeight = image.size[1] + abs(offset[1]) + 2*border

    #Create the shadow's image. Match the parent image's mode.
    shadow = Image.new("RGBA", (fullWidth, fullHeight), backgroundColour)

    # Place the shadow, with the required offset
    shadowLeft = border + max(offset[0], 0)
    shadowTop  = border + max(offset[1], 0)
    #Paste in the constant colour
    shadow.paste(shadowColour,
                [shadowLeft, shadowTop,
                 shadowLeft + image.size[0],
                 shadowTop  + image.size[1] ], image)

    # Apply the BLUR filter repeatedly
    for i in range(iterations):
        shadow = shadow.filter(ImageFilter.BLUR)

    # Paste the original image on top of the shadow
    imgLeft = border - min(offset[0], 0)
    imgTop  = border - min(offset[1], 0)
    shadow.paste(image, (imgLeft, imgTop), image)

    return resizeImageAbs(shadow, originalSize[0], originalSize[1])

'''
Resize an image with desired dimensions. This is most suitable for resizing non
square images where a factor would not be sufficient
'''
def resizeImageAbs(image, width, height):
    return image.resize((width, height), Image.ANTIALIAS)

'''
Resize a square image. Or make a non square image square (will stretch if input
image is non-square)
'''
def resizeImageSquare(image, size):
    return resizeImageAbs(image, size, size)

'''
Resize an image by a factor. eg 2 will double the image dimensions, 0.5 would
halve them
'''
def resizeImage(image, factor):
    return resizeImageAbs(image,int(image.width*factor), int(image.height*factor))

'''
Round Corners taking a radius int as an arg and do antialias
'''
def roundCornersAntiAlias(image, radius):
    FACTOR = 2
    imageTemp = resizeImage(image, FACTOR)
    imageTemp = roundCorners(imageTemp, radius * FACTOR)
    return resizeImage(imageTemp, 1/FACTOR)

'''
Round Corners taking a Percentage int as an arg (eg. 50 > 50%) and do
antialias
'''
def roundCornersPercentAntiAlias(image, radius):
    FACTOR = 2
    imageTemp = resizeImage(image, FACTOR)
    imageTemp = roundCornersPercent(imageTemp, radius * FACTOR)
    return resizeImage(imageTemp, 1/FACTOR)

'''
Opens all images in a directory and returns them in a list along with
filepath. args in the form "input/*."
Use full file path or file path relative to /lib
'''
def openImagesInDir(dir):
    images = []
    for fileExt in FILE_EXTS:
        for file in glob.glob(dir + "." + fileExt):
            images.append((file,Image.open(file)))
    return images



'''
Opens a single image and returns an image object.
Use full file path or file path relative to /lib
'''
def openImage(file):
    return Image.open(file)


'''
Saves a single image.
Use full file path or file path relative to /lib. Pass in the image object
'''
def saveImage(fileName, image, optimise=True):
    createDirsIfRequired(fileName)
    if optimise:
        image = image.convert('P', palette=Image.ADAPTIVE, colors=255)
    image.save(fileName, optimize=optimise, quality=75)

'''
Create directories if required when writing a file
'''
def createDirsIfRequired(filepath):
    import re, os
    tok = re.split('/|\\\\', filepath)
    checkfile = ''
    for x in tok[:-1]:
        checkfile += x + '\\'
    os.makedirs(checkfile, exist_ok=True)

'''
Takes an image and preforms a centre crop and removes the padding
'''
def removeImagePadding(image, padding):
    return image.crop((padding, padding, image.width -padding, image.height -padding))

'''
Gets an image description returns [icon/mask]

Likely more useful for my specific use case than in the general lib
'''
def getImageDesc(image):
    if (image.width == 640 and image.height == 640):
        return "mask"
    elif (image.width == 512 and image.height == 512):
        return "icon"
