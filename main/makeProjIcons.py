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
from metprint import Logger, LogType, FHFormatter
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imageedit import io, transform, effects

if __name__ == "__main__": # pragma: no cover

	# Image in should be 512px
	images = io.openImagesInDir(THISDIR + "/input/*", "logo")
	for imageRef in images:
		fileName, squareImage = imageRef
		fileNameParts = fileName.split(os.sep)
		fileName = fileNameParts[len(fileNameParts) - 1]
		Logger(FHFormatter()).logPrint(fileName, LogType.BOLD)
		outputDir = THISDIR + "/output/" + fileName + "/proj-icon"

		# Proj-icon does not want to be a mask

		if (io.getImageDesc(squareImage) == "mask"):
			textName = fileName.split('.')[0]
			io.saveImage(
			outputDir + "/name.png",
			effects.addDropShadowSimple(
			effects.roundCornersAntiAlias(
			transform.resizeSquare(effects.addText(squareImage, textName), "0.5x"), 64),
			[-10, 10]))

			squareImage = transform.removePadding(squareImage, 64)

		roundImage = effects.roundCornersAntiAlias(squareImage, 256)
		squircleImage = effects.roundCornersAntiAlias(squareImage, 102) # Google Play Rounding

		# store-google-play-raster - Drop shadow, radius 20% (102,51)
		googlePlay = effects.addDropShadowSimple(squircleImage, [-10, 10])
		io.saveImage(outputDir + "/proj-icon.png", transform.resizeSquare(googlePlay, 256))
		'''
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(squircleImage, 256))
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(roundImage, 256))
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(squareImage, 256))
		'''
