'''
Author FredHappyface 20190918
Make Images for PWAs
'''
import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imageedit import imagetracer
from imageedit import imageedit

if __name__ == "__main__": # pragma: no cover

	# Image in should be 512px
	images = imageedit.openImagesInDir(THISDIR + "/input/*")
	for imageRef in images:
		fileName, squareImage = imageRef
		fileNameParts = fileName.split(os.sep)
		fileName = fileNameParts[len(fileNameParts)-1]
		imageedit.logPrint(fileName, "bold")
		outputDir = THISDIR + "/output/" + fileName
		storeDir = outputDir + "/store"
		pwaDir = outputDir + "/pwa"

		# Create a mask image and then convert to icon
		if (imageedit.getImageDesc(squareImage) == "mask"):
			imageedit.saveImage(pwaDir + "/mask.png", imageedit.resizeImageSquare(squareImage, 512))
			squareImage = imageedit.removeImagePadding(squareImage, 64)


		roundImage = imageedit.roundCornersAntiAlias(squareImage, 256)
		squircleImage = imageedit.roundCornersAntiAlias(squareImage, 102) # Google Play Rounding

		'''
		Store Images
		'''

		# store-windows - Size 300px
		imageedit.saveImage(storeDir + "/store-windows.png",
			imageedit.resizeImageSquare(squareImage, "0.5859375x"))
		# store-google-play - Size 512, png32
		imageedit.saveImage(storeDir + "/store-google-play.png", squareImage, False)
		# store-ios - Size 180px
		imageedit.saveImage(storeDir + "/store-ios.png",
		imageedit.resizeImageSquare(squareImage, "0.3515625x"))

		# store-google-play-raster - Drop shadow, radius 20% (102,51)
		googlePlay = imageedit.addDropShadowSimple(squircleImage, [-10, 10])
		imageedit.saveImage(storeDir + "/store-google-play-raster.png",
			imageedit.resizeImageSquare(googlePlay, "0.5x"))

		# store-ios-raster - Radius 17.5% (90,45)
		ios = imageedit.roundCornersAntiAlias(squareImage, 90)
		imageedit.saveImage(storeDir + "/store-ios-raster.png",
			imageedit.resizeImageSquare(ios, "0.5x"))

		# store-windows-raster
		imageedit.saveImage(storeDir + "/store-windows-raster.png",
			imageedit.resizeImageSquare(squareImage, "0.5x"))


		'''
		PWA Images
		'''
		imageedit.saveImage(pwaDir + "/squircle-256.png", imageedit.resizeImageSquare(squircleImage, 256))
		imageedit.saveImage(pwaDir + "/round-512.png", roundImage)
		imageedit.saveImage(pwaDir + "/round-192.png", imageedit.resizeImageSquare(roundImage, 192))
		# imageedit.saveImage(pwaDir + "/square-512.png", squareImage) # 'raw'
		smallSquare = imageedit.resizeImageSquare(squareImage, 180)
		imageedit.saveImage(pwaDir + "/square-180.png", smallSquare)

		logoBW = imageedit.convertBlackAndWhite(squareImage, "foreground")
		imageedit.saveImage(pwaDir + "/logo-bw.png", logoBW)
		open(pwaDir + "/safari.svg", "w").write(imagetracer.trace(pwaDir + "/logo-bw.png", True))
