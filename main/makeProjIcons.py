#!/usr/bin/env python3
'''
Author FredHappyface 20190918

Make GitHub project icons, does a bit more than round.py. At the moment, I quite
fancy using images in a similar style to those used in the google play store.
Other commented alternatives are, square, squircle (no shadow) and circle
'''

import os, sys
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR) + "/lib")
import imageEdit

if __name__ == "__main__": # pragma: no cover

	# Image in should be 512px
	images = imageEdit.openImagesInDir(THISDIR + "/input/*", "logo")
	for imageRef in images:
		fileName, squareImage = imageRef
		fileNameParts = fileName.split(os.sep)
		fileName = fileNameParts[len(fileNameParts)-1]
		imageEdit.logPrint(fileName, "bold")
		outputDir = THISDIR + "/output/" + fileName + "/proj-icon"

		# Proj-icon does not want to be a mask

		if (imageEdit.getImageDesc(squareImage) == "mask"):
			textName = fileName.split('.')[0]
			imageEdit.saveImage(outputDir + "/name.png",
				imageEdit.addDropShadowSimple(
					imageEdit.roundCornersAntiAlias(
						imageEdit.resizeImageSquare(
							imageEdit.addText(squareImage, textName),
						"0.5x"),
					64),
				[-10, 10])
			)


			squareImage = imageEdit.removeImagePadding(squareImage, 64)


		roundImage = imageEdit.roundCornersAntiAlias(squareImage, 256)
		squircleImage = imageEdit.roundCornersAntiAlias(squareImage, 102) # Google Play Rounding

		# store-google-play-raster - Drop shadow, radius 20% (102,51)
		googlePlay = imageEdit.addDropShadowSimple(squircleImage, [-10, 10])
		imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(googlePlay, 256))

		'''
		imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(squircleImage, 256))
		imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(roundImage, 256))
		imageEdit.saveImage(outputDir + "/proj-icon.png", imageEdit.resizeImageSquare(squareImage, 256))
		'''
