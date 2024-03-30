"""
Author FredHappyface

Test imageedit.py with a single 512x512px image. Many of these tests need manual
validattransformn. Look at each test for a brief descripttransformn of the desired outcome for
each test
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

from imageedit import io, transform

INPUT = f"{THISDIR}/test_transform/i"
OUTPUT = f"{THISDIR}/test_transform/o"

IMAGE = io.openImage(INPUT + "/test.png")


def test_cropCentre() -> None:
	"""
	Manual Check
	Desired Output: A square image 256x256 pixels
	"""
	io.saveImage(OUTPUT + "/test_cropCentre.png", transform.cropCentre(IMAGE, 256, 256))


def test_uncrop() -> None:
	"""
	Manual Check
	Desired Output: An 'uncropped' image of a field
	"""
	io.saveImage(
		OUTPUT + "/test_uncrop.png",
		transform.expand(io.openImage(INPUT + "/test_field.png"), 64),
	)


def test_resizeImageAbs_256x256() -> None:
	assert transform.resize(IMAGE, 256, 256).size == (256, 256)


def test_resizeImageAbs_512x256() -> None:
	assert transform.resize(IMAGE, 512, 256).size == (512, 256)


def test_resizeImageAbs_256x512() -> None:
	assert transform.resize(IMAGE, 256, 512).size == (256, 512)


def test_resizeSquare_1024() -> None:
	assert transform.resizeSquare(IMAGE, 1024).size == (1024, 1024)


def test_resizeSquare_256() -> None:
	assert transform.resizeSquare(IMAGE, 256).size == (256, 256)


def test_resizeImage_x2() -> None:
	assert transform.resizeSquare(IMAGE, "2x").size == (1024, 1024)


def test_resizeImage_x0_5() -> None:
	assert transform.resizeSquare(IMAGE, "0.5x").size == (256, 256)


def test_removeImagePadding_0() -> None:
	assert transform.removePadding(IMAGE, 0).size == (512, 512)


def test_removeImagePadding_100() -> None:
	assert transform.removePadding(IMAGE, 100).size == (312, 312)
