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
		pwaDir = outputDir + "/pwa"

		# Create a mask image and then convert to icon
		if (imageEdit.getImageDesc(squareImage) == "mask"):
			imageEdit.saveImage(pwaDir + "/mask.png", imageEdit.resizeImageSquare(squareImage, 512))
			squareImage = imageEdit.removeImagePadding(squareImage, 64)


		roundImage = imageEdit.roundCornersAntiAlias(squareImage, 256)
		squircleImage = imageEdit.roundCornersAntiAlias(squareImage, 102) # Google Play Rounding

		'''
		Store Images
		'''
		# store-windows - Size 300px
		imageEdit.saveImage(storeDir + "/store-windows.png",
			imageEdit.resizeImage(squareImage, 0.5859375))
		# store-google-play - Size 512, png32
		imageEdit.saveImage(storeDir + "/store-google-play.png", squareImage, False)
		# store-ios - Size 180px
		imageEdit.saveImage(storeDir + "/store-ios.png", imageEdit.resizeImage(squareImage, 0.3515625))

		# store-google-play-raster - Drop shadow, radius 20% (102,51)
		googlePlay = imageEdit.addDropShadowSimple(squircleImage, [-10, 10])
		imageEdit.saveImage(storeDir + "/store-google-play-raster.png", googlePlay)
		imageEdit.saveImage(storeDir + "/store-google-play-raster-small.png",
			imageEdit.resizeImage(googlePlay, 0.5))

		# store-ios-raster - Radius 17.5% (90,45)
		ios = imageEdit.roundCornersAntiAlias(squareImage, 90)
		imageEdit.saveImage(storeDir + "/store-ios-raster.png", ios)
		imageEdit.saveImage(storeDir + "/store-ios-raster-small.png",
			imageEdit.resizeImage(ios, 0.5))

		# store-windows-raster
		imageEdit.saveImage(storeDir + "/store-windows-raster.png", squareImage)
		imageEdit.saveImage(storeDir + "/store-windows-raster-small.png",
			imageEdit.resizeImage(squareImage, 0.5))


		'''
		PWA Images
		'''
		imageEdit.saveImage(pwaDir + "/squircle-256.png", imageEdit.resizeImageSquare(squircleImage, 256))
		imageEdit.saveImage(pwaDir + "/round-512.png", roundImage)
		imageEdit.saveImage(pwaDir + "/round-192.png", imageEdit.resizeImageSquare(roundImage, 192))
		# imageEdit.saveImage(pwaDir + "/square-512.png", squareImage) # 'raw'
		imageEdit.saveImage(pwaDir + "/square-180.png", imageEdit.resizeImageSquare(squareImage, 180))

		'''
		Proposals:

		squircle image is used for favicons so can be smaller: 128px
		imageEdit.saveImage(pwaDir + "/squircle-128.png", imageEdit.resizeImageSquare(squircleImage, 128))

		'''
