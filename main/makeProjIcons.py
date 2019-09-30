'''
Author FredHappyface 20190918

Make GitHub project icons, does a bit more than round.py. At the moment, I quite
fancy using images in a similar style to those used in the google play store.

Other commented alternatines are, square, squircle (no shadow) and circle
'''

import os, sys, inspect
THISDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, os.path.dirname(THISDIR) + "/lib")
import imageEdit

if __name__ == "__main__": # pragma: no cover

    # Image in should be 512px
    images = imageEdit.openImagesInDir(THISDIR + "/input/*")
    for imageRef in images:
        fileName, squareImage = imageRef
        fileNameParts = fileName.split("\\")
        fileName = fileNameParts[len(fileNameParts)-1]
        print(fileName)
        outputDir = THISDIR + "/output/" + fileName + "/proj-icon"

        # Proj-icon does not want to be a mask
        if (imageEdit.getImageDesc(squareImage) == "mask"):
            squareImage = imageEdit.removeImagePadding(squareImage, 64)

        roundImage = imageEdit.roundCornersAntiAlias(squareImage, 256)
        squircleImage = imageEdit.roundCornersAntiAlias(squareImage, 102) # Google Play Rounding

        # store-google-play-raster - Drop shadow, radius 20% (102,51)
        googlePlay = imageEdit.addDropShadowSimple(squircleImage, [-10,10])
        imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(googlePlay, 256))

        '''
        imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(squircleImage, 256))
        imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(roundImage, 256))
        imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(squareImage, 256))
        '''
