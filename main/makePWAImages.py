'''
Author FredHappyface 20190918

Make Images for PWAs
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
        outputDir = THISDIR + "/output/" + fileName
        storeDir = outputDir + "/store"
        fullDir = outputDir + "/full"

        roundImage = imageEdit.roundCornersAntiAlias(squareImage, 256)
        squircleImage = imageEdit.roundCornersAntiAlias(squareImage, 102) # Google Play Rounding

        '''
        Store Images
        '''
        # store-windows - Size 300px
        imageEdit.saveImage(storeDir + "/store-windows.png", imageEdit.resizeImage(squareImage, 0.5859375))
        # store-google-play - Size 512, png32
        imageEdit.saveImage(storeDir + "/store-google-play.png", squareImage, False)
        # store-ios - Size 180px
        imageEdit.saveImage(storeDir + "/store-ios.png", imageEdit.resizeImage(squareImage, 0.3515625))

        # store-google-play-raster - Drop shadow, radius 20% (102,51)
        googlePlay = imageEdit.addDropShadowSimple(squircleImage, [2,15])
        imageEdit.saveImage(storeDir + "/store-google-play-raster.png", googlePlay)
        imageEdit.saveImage(storeDir + "/store-google-play-raster-small.png", imageEdit.resizeImage(googlePlay, 0.5))

        # store-ios-raster - Radius 17.5% (90,45)
        ios = imageEdit.roundCornersAntiAlias(squareImage, 90)
        imageEdit.saveImage(storeDir + "/store-ios-raster.png", ios)
        imageEdit.saveImage(storeDir + "/store-ios-raster-small.png", imageEdit.resizeImage(ios, 0.5))

        # store-windows-raster
        imageEdit.saveImage(storeDir + "/store-windows-raster.png", squareImage)
        imageEdit.saveImage(storeDir + "/store-windows-raster-small.png", imageEdit.resizeImage(squareImage, 0.5))


        '''
        PWA Images
        '''
        # RAW
        imageEdit.saveImage(fullDir + "/raw.png", squareImage)
        # android-icon-512x512
        imageEdit.saveImage(fullDir + "/android-icon-512x512.png", roundImage)
        # android-icon-192x192
        imageEdit.saveImage(fullDir + "/android-icon-192x192.png", imageEdit.resizeImage(roundImage, 0.375))
        # apple-icon-180x180
        imageEdit.saveImage(fullDir + "/apple-icon-180x180.png", imageEdit.resizeImage(squareImage, 0.3515625))

        # favicon-32x32
        imageEdit.saveImage(fullDir + "/favicon-32x32.png", imageEdit.resizeImage(squircleImage, 0.0625))
        # favicon-16x16
        imageEdit.saveImage(fullDir + "/favicon-16x16.png", imageEdit.resizeImage(squircleImage, 0.03125))

        # ms-icon-70x70
        imageEdit.saveImage(fullDir + "/ms-icon-70x70.png", imageEdit.resizeImage(squareImage, 0.13671875))
        # ms-icon-150x150
        imageEdit.saveImage(fullDir + "/ms-icon-150x150.png", imageEdit.resizeImage(squareImage, 0.29296875))
        # ms-icon-310x310
        imageEdit.saveImage(fullDir + "/ms-icon-310x310.png", imageEdit.resizeImage(squareImage, 0.60546875))

        '''
        Proposal Images
        '''
        imageEdit.saveImage(outputDir + "/squircle-256.png", imageEdit.resizeImageSquare(squircleImage, 256))
        imageEdit.saveImage(outputDir + "/round-512.png", roundImage)
        imageEdit.saveImage(outputDir + "/round-192.png", imageEdit.resizeImageSquare(roundImage, 192))
        imageEdit.saveImage(outputDir + "/square-512.png", squareImage)
        imageEdit.saveImage(outputDir + "/square-180.png", imageEdit.resizeImageSquare(squareImage, 180))
