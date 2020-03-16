#!/usr/bin/env python3
'''
Author FredHappyface 20190918

Make GitHub project icons, does a bit more than round.py. At the moment, I quite
fancy using images in a similar style to those used in the google play store.
Other commented alternatives are, square, squircle (no shadow) and circle
'''

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imageedit import imageedit

if __name__ == "__main__": # pragma: no cover

	# Image in should be 512px
	images = imageedit.openImagesInDir(THISDIR + "/input/*", "logo")
	for imageRef in images:
		fileName, squareImage = imageRef
		fileNameParts = fileName.split(os.sep)
		fileName = fileNameParts[len(fileNameParts)-1]
		imageedit.logPrint(fileName, "bold")
		outputDir = THISDIR + "/output/" + fileName + "/proj-icon"

		# Proj-icon does not want to be a mask

		if (imageedit.getImageDesc(squareImage) == "mask"):
			textName = fileName.split('.')[0]
			imageedit.saveImage(outputDir + "/name.png",
				imageedit.addDropShadowSimple(
					imageedit.roundCornersAntiAlias(
						imageedit.resizeImageSquare(
							imageedit.addText(squareImage, textName),
						"0.5x"),
					64),
				[-10, 10])
			)


			squareImage = imageedit.removeImagePadding(squareImage, 64)


		roundImage = imageedit.roundCornersAntiAlias(squareImage, 256)
		squircleImage = imageedit.roundCornersAntiAlias(squareImage, 102) # Google Play Rounding

		# store-google-play-raster - Drop shadow, radius 20% (102,51)
		googlePlay = imageedit.addDropShadowSimple(squircleImage, [-10, 10])
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(googlePlay, 256))

		'''
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(squircleImage, 256))
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(roundImage, 256))
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(squareImage, 256))
		'''
