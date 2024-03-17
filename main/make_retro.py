"""Author FredHappyface 2019-2022

Make Images for PWAs
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from blendmodes.blend import BlendType
from layeredimage.layeredimage import Layer, LayeredImage

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
		outputDir = f"{THISDIR}/output/" + fileName
		retroDir = outputDir + "/retro"
		if io.getImageDesc(squareImage) == "mask":
			squareImage = transform.removePadding(squareImage, 64)
		roundImage = effects.roundCornersAntiAlias(squareImage, 256)
		squircleImage = effects.roundCornersAntiAlias(squareImage, 102)  # Google Play Rounding
		"""
		Retro Images
		"""
		# BBC Micro (3bitrgb)
		swatch = effects.applySwatch(
			effects.pixelate(squareImage), f"{THISDIR}/resources/3bitrgb.png"
		)
		io.saveImage(retroDir + "/bbc-micro.png", transform.resizeSquare(swatch, "0.5x"))
		# Pebble Smartwatch (6bitrgb)
		swatch = effects.applySwatch(squareImage, f"{THISDIR}/resources/6bitrgb.png")
		io.saveImage(retroDir + "/pebble-smartwatch.png", transform.resizeSquare(swatch, "0.5x"))
		# ZX Spectrum (4bitrgb)
		swatch = effects.applySwatch(
			effects.pixelate(squareImage), f"{THISDIR}/resources/4bitrgb.png"
		)
		io.saveImage(retroDir + "/zxspectrum.png", transform.resizeSquare(swatch, "0.5x"))
		# 3-Level RGB
		swatch = effects.applySwatch(
			effects.pixelate(squareImage), f"{THISDIR}/resources/3levelrgb.png"
		)
		io.saveImage(retroDir + "/3level.png", transform.resizeSquare(swatch, "0.5x"))
		# websafe
		swatch = effects.applySwatch(squareImage, f"{THISDIR}/resources/web.gpl")
		io.saveImage(retroDir + "/websafe.png", transform.resizeSquare(swatch, "0.5x"))
		# ios6
		ios = effects.roundCornersAntiAlias(squareImage, 90)
		ios6 = io.exportFlatImage(
			retroDir + "/ios1.png",
			LayeredImage(
				[
					Layer("bg", ios),
					Layer("overlay", io.openImage(f"{THISDIR}/resources/ios6_2.png")),
				]
			),
		)
		# ios7 - Radius 17.5% (90,45)
		io.saveImage(retroDir + "/ios7.png", transform.resizeSquare(ios, "0.5x"))
		# Android < 5
		io.saveImage(
			retroDir + "/android2.png",
			transform.resizeSquare(
				effects.blend(
					effects.removeBG(squareImage),
					io.openImage(f"{THISDIR}/resources/android_legacy.png"),
					BlendType.SRCATOP,
				),
				"0.5x",
			),
		)
		# Android 6
		swatch = effects.applySwatch(squareImage, f"{THISDIR}/resources/material-mini.gpl")
		io.saveImage(
			retroDir + "/android6.png",
			transform.resizeSquare(effects.removeBG(swatch), "0.5x"),
		)
		# Android 7
		swatch = effects.applySwatch(roundImage, f"{THISDIR}/resources/material-mini.gpl")
		io.saveImage(retroDir + "/android7.png", transform.resizeSquare(swatch, "0.5x"))
		# Android 8+
		swatch = effects.applySwatch(squareImage, f"{THISDIR}/resources/material-mini.gpl")
		io.saveImage(retroDir + "/android8.png", transform.resizeSquare(swatch, "0.5x"))
		# Papirus/ Paper Icons
		swatch = effects.applySwatch(ios, f"{THISDIR}/resources/papirus.gpl")
		io.saveImage(retroDir + "/papirus.png", transform.resizeSquare(swatch, "0.5x"))
		# OneDark
		swatch = effects.applySwatch(squircleImage, f"{THISDIR}/resources/base24.yaml")
		io.saveImage(retroDir + "/onedark.png", transform.resizeSquare(swatch, "0.5x"))
