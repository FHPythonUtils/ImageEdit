"""
Author Kieran W 2019-05-07
Round the corners of an image
"""

import argparse
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from imageedit import effects, io

if __name__ == "__main__":  # pragma: no cover
	# Command line arguments. Author Kieran
	parser = argparse.ArgumentParser(description="Round the corners of an image")
	parser.add_argument("-i", "--image", help="specify the path to an input image", action="store")
	parser.add_argument(
		"-o", "--output", help="specify the path to an output image", action="store"
	)
	parser.add_argument(
		"-r",
		"--radius",
		help="specify the corner radius (image w/l /2 for a round image)",
		action="store",
	)
	parser.add_argument(
		"-b",
		"--batch",
		help="batch process files. requires input and output directories",
		action="store_true",
	)

	args = parser.parse_args()

	if args.batch:
		images = io.openImagesInDir(THISDIR + "/input/*")
		print(images)
		for imageRef in images:
			fileName, image = imageRef
			fileNameParts = fileName.split("\\")
			fileName = fileNameParts[len(fileNameParts) - 1]
			print(fileName)
			if args.radius is not None:
				image = effects.roundCorners(image, int(args.radius))
			else:
				image = effects.roundCorners(image, int(image.width / 2))
			io.saveImage(THISDIR + "/output/out-" + fileName, image)

	else:
		im = io.openImage(THISDIR + "/" + args.image)
		if args.radius is not None:
			im = effects.roundCorners(im, int(args.radius))
		else:
			im = effects.roundCorners(im, int(im.width / 2))

		if args.output is not None:
			outFileName = args.output
		else:
			outFileName = args.image
		io.saveImage(THISDIR + "/" + outFileName, im)
