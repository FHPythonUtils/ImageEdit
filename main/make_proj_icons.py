"""Author FredHappyface 2019-2022

Make GitHub project icons, does a bit more than round.py. At the moment, I quite
fancy using images in a similar style to those used in the google play store.
Other commented alternatives are, square, squircle (no shadow) and circle
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from imageedit import effects, io, transform

if __name__ == "__main__":  # pragma: no cover

	# Image in should be 512px
	images = io.openImagesInDir(f"{THISDIR}/input/*")
	for imageRef in images:
		fileName, squareImage = imageRef
		fileNameParts = fileName.split(os.sep)
		fileName = fileNameParts[len(fileNameParts) - 1]
		print(fileName)
		print(f"getContrastRatio: {io.getContrastRatio(squareImage)}")
		outputDir = f"{THISDIR}/output/" + fileName + "/proj-icon"

		# Proj-icon does not want to be a mask

		if io.getImageDesc(squareImage) == "mask":
			textName = fileName.split(".")[0]
			io.saveImage(
				outputDir + "/name.png",
				effects.addDropShadowSimple(
					effects.roundCornersAntiAlias(
						transform.resizeSquare(effects.addText(squareImage, textName), "0.5x"), 64
					),
					[-10, 10],
				),
			)

			squareImage = transform.removePadding(squareImage, 64)

		roundImage = effects.roundCornersAntiAlias(squareImage, 256)
		squircleImage = effects.roundCornersAntiAlias(squareImage, 102)  # Google Play Rounding

		# store-google-play-raster - Drop shadow, radius 20% (102,51)
		googlePlay = effects.addDropShadowSimple(squircleImage, [-10, 10])
		io.saveImage(outputDir + "/proj-icon.png", transform.resizeSquare(googlePlay, 256))
		"""
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(squircleImage, 256))
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(roundImage, 256))
		imageedit.saveImage(outputDir + "/proj-icon.png", imageedit.resizeImageSquare(squareImage, 256))
		"""
