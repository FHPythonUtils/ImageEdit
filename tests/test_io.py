"""
Author FredHappyface

Test io.py with a single 512x512px image. Many of these tests need manual
validation. Look at each test for a brief description of the desired outcome for
each test
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from PIL import Image

from imageedit import io, transform

INPUT = f"{THISDIR}/test_io/i"
OUTPUT = f"{THISDIR}/test_io/o"

IMAGE = io.openImage(INPUT + "/test.png")


def test_reduceColours_optimised() -> None:
	"""
	Won't be able to see difference but will be able to .getcolors with maxcolors 256
	"""
	assert not isinstance(
		io.reduceColours(io.openImage(INPUT + "/test_field.png"), "optimised").getcolors(
			maxcolors=256
		),
		type(None),
	)


def test_reduceColours_logo() -> None:
	"""
	.getcolors with maxcolors 16
	"""
	assert not isinstance(
		io.reduceColours(io.openImage(INPUT + "/test_field.png"), "logo").getcolors(maxcolors=16),
		type(None),
	)


def test_getPixelDimens_px() -> None:
	assert io.getPixelDimens(IMAGE, [256]), [256]


def test_getPixelDimens_scale() -> None:
	assert io.getPixelDimens(IMAGE, ["0.5x"]), [256]


def test_getPixelDimens_percent() -> None:
	assert io.getPixelDimens(IMAGE, ["50%"]), [256]


def test_openImagesInDir() -> None:
	assert len(io.openImagesInDir(INPUT + "/*")) == 2


def test_openImagesInDir_optimised() -> None:
	assert len(io.openImagesInDir(INPUT + "/*")) == 2


def test_openImage() -> None:
	assert isinstance(io.openImage(INPUT + "/test.png"), Image.Image)


def test_openImage_optimised() -> None:
	assert isinstance(io.openImage(INPUT + "/test.png", "optimised"), Image.Image)


def test_getImageDesc_icon() -> None:
	assert io.getImageDesc(IMAGE) == "icon"


def test_getImageDesc_mask() -> None:
	assert io.getImageDesc(transform.resizeSquare(IMAGE, 640)) == "mask"


def test_getImageDesc_null() -> None:
	assert io.getImageDesc(transform.resizeSquare(IMAGE, 256)) == "unknown"


"""
def test_getSortedColours_none():
	assert(io.getSortedColours(io.openImage(INPUT+ "/test_field.png")) == [(1, (255, 255, 255, 255)), (1, (1, 1, 1, 255))])
"""
