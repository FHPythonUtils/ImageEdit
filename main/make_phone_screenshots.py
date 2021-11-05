"""Author FredHappyface 2021...

Make Android screenshots look nice and create a cover image for google play store
"""
import os
import sys
from pathlib import Path

from layeredimage.layeredimage import Layer, LayeredImage
from metprint import FHFormatter, Logger, LogType
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from imageedit import effects, io

if __name__ == "__main__":  # pragma: no cover

	OUTPUT_DIR = THISDIR + "/output/screenshots/"
	OVERLAY = io.openImage(THISDIR + "/resources/pixel3aScreenshot_8colours.png")

	# Create cover image/ featureGraphic
	coverImages = io.openImagesInDir(THISDIR + "/input/*-playstore")
	if len(coverImages) > 0:
		_, srcImage = coverImages[0]
		coverImage = Image.new("RGBA", (1024, 500), srcImage.getpixel((0, 0)))
		coverImage.paste(srcImage, (256, -6))
		io.saveImage(
			OUTPUT_DIR + "featureGraphic.png",
			coverImage,
		)
		Logger(FHFormatter()).logPrint("::Created Cover Image::", LogType.BOLD)

	# Process screenshots
	images = io.openImagesInDir(THISDIR + "/input/*")
	for imageRef in images:
		fileName, screenshot = imageRef
		fileNameParts = fileName.split(os.sep)
		fileName = fileNameParts[len(fileNameParts) - 1]
		Logger(FHFormatter()).logPrint(fileName, LogType.BOLD)
		os.makedirs(OUTPUT_DIR, exist_ok=True)
		composite = effects.resize(
			LayeredImage(
				[
					Layer(
						"bg",
						Image.new(
							"RGBA", (OVERLAY.width, OVERLAY.height), screenshot.getpixel((50, 100))
						),
					),
					Layer("screenshot", screenshot, offsets=(525, 770)),
					Layer("overlay", OVERLAY),
				]
			).getFlattenLayers(),
			"50%",
			"50%",
		)
		io.saveImage(OUTPUT_DIR + fileName, composite)
