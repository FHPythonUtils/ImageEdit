"""
Author FredHappyface 20190930

Test imageedit.py with a single 512x512px image. Many of these tests need manual
validattransformn. Look at each test for a brief descripttransformn of the desired outcome for
each test
"""

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

from imageedit import io, transform

INPUT = THISDIR + "/test_transform/i"
OUTPUT = THISDIR + "/test_transform/o"

IMAGE = io.openImage(INPUT + "/test.png")


def test_cropCentre():
	"""
	Manual Check
	Desired Output: A square image 256x256 pixels
	"""
	io.saveImage(OUTPUT + "/test_cropCentre.png", transform.cropCentre(IMAGE, 256, 256))


def test_uncrop():
	"""
	Manual Check
	Desired Output: An 'uncropped' image of a field
	"""
	io.saveImage(
		OUTPUT + "/test_uncrop.png", transform.expand(io.openImage(INPUT + "/test_field.png"), 64)
	)


def test_resizeImageAbs_256x256():
	assert transform.resize(IMAGE, 256, 256).size == (256, 256)


def test_resizeImageAbs_512x256():
	assert transform.resize(IMAGE, 512, 256).size == (512, 256)


def test_resizeImageAbs_256x512():
	assert transform.resize(IMAGE, 256, 512).size == (256, 512)


def test_resizeSquare_1024():
	assert transform.resizeSquare(IMAGE, 1024).size == (1024, 1024)


def test_resizeSquare_256():
	assert transform.resizeSquare(IMAGE, 256).size == (256, 256)


def test_resizeImage_x2():
	assert transform.resizeSquare(IMAGE, "2x").size == (1024, 1024)


def test_resizeImage_x0_5():
	assert transform.resizeSquare(IMAGE, "0.5x").size == (256, 256)


def test_removeImagePadding_0():
	assert transform.removePadding(IMAGE, 0).size == (512, 512)


def test_removeImagePadding_100():
	assert transform.removePadding(IMAGE, 100).size == (312, 312)
