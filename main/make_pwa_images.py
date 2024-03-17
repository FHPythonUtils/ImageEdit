"""
Author FredHappyface 2019-2022
Make Images for PWAs
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from imageedit import effects, imagetracer, io, transform

if __name__ == "__main__":  # pragma: no cover
	# Image in should be 512px
	images = io.openImagesInDir(f"{THISDIR}/input/*")
	for imageRef in images:
		fileName, squareImage = imageRef
		fileNameParts = fileName.split(os.sep)
		fileName = fileNameParts[len(fileNameParts) - 1]
		print(fileName)
		print(f"getContrastRatio: {io.getContrastRatio(squareImage)}")
		outputDir = f"{THISDIR}/output/{fileName}"
		storeDir = outputDir + "/store"
		pwaDir = outputDir + "/pwa"

		# Create a mask image and then convert to icon
		if io.getImageDesc(squareImage) == "mask":
			io.saveImage(f"{pwaDir}/mask.png", transform.resizeSquare(squareImage, 512))
			squareImage = transform.removePadding(squareImage, 64)

		roundImage = effects.roundCornersAntiAlias(squareImage, 256)
		squircleImage = effects.roundCornersAntiAlias(squareImage, 102)  # Google Play Rounding
		"""
		Store Images
		"""

		# store-windows - Size 300px
		io.saveImage(
			f"{storeDir}/store-windows.png",
			transform.resizeSquare(squareImage, "0.5859375x"),
		)
		# store-google-play - Size 512, png32
		io.saveImage(f"{storeDir}/store-google-play.png", squareImage)
		# store-ios - Size 180px
		io.saveImage(
			f"{storeDir}/store-ios.png",
			transform.resizeSquare(squareImage, "0.3515625x"),
		)

		# store-google-play-raster - Drop shadow, radius 20% (102,51)
		googlePlay = effects.addDropShadowSimple(squircleImage, [-10, 10])
		io.saveImage(
			f"{storeDir}/store-google-play-raster.png",
			transform.resizeSquare(googlePlay, "0.5x"),
		)

		# store-ios-raster - Radius 17.5% (90,45)
		ios = effects.roundCornersAntiAlias(squareImage, 90)
		io.saveImage(f"{storeDir}/store-ios-raster.png", transform.resizeSquare(ios, "0.5x"))

		# store-windows-raster
		io.saveImage(
			f"{storeDir}/store-windows-raster.png",
			transform.resizeSquare(squareImage, "0.5x"),
		)
		"""
		PWA Images
		"""
		io.saveImage(f"{pwaDir}/squircle-256.png", transform.resizeSquare(squircleImage, 256))
		io.saveImage(f"{pwaDir}/round-512.png", roundImage)
		io.saveImage(f"{pwaDir}/round-192.png", transform.resizeSquare(roundImage, 192))
		# imageedit.saveImage(f"{pwaDir}/square-512.png", squareImage) # 'raw'
		smallSquare = transform.resizeSquare(squareImage, 180)
		io.saveImage(f"{pwaDir}/square-180.png", smallSquare)

		logoBW = effects.convertBlackAndWhite(squareImage, "foreground")
		io.saveImage(f"{pwaDir}/logo-bw.png", logoBW)
		Path(f"{pwaDir}/safari.svg").write_text(
			imagetracer.trace(f"{pwaDir}/logo-bw.png", True), encoding="utf-8"
		)
