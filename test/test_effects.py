"""
Author FredHappyface 20190930

Test imageedit.py with a single 512x512px image. Many of these tests need manual
validation. Look at each test for a brief description of the desired outcome for
each test
"""

import os
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

from imageedit import effects, io

INPUT = THISDIR + "/test_effects/i"
OUTPUT = THISDIR + "/test_effects/o"

IMAGE = io.openImage(INPUT + "/test.png")


def test_roundCornersPercent_0():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels
	"""
	io.saveImage(OUTPUT + "/test_roundCornersPercent_0.png", effects.roundCorners(IMAGE, "0%"))


def test_roundCornersPercent_50():
	"""
	Manual Check
	Desired Output: A circular image 512x512 pixels
	"""
	io.saveImage(OUTPUT + "/test_roundCornersPercent_50.png", effects.roundCorners(IMAGE, "50%"))


def test_roundCorners_0():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels
	"""
	io.saveImage(OUTPUT + "/test_roundCorners_0.png", effects.roundCorners(IMAGE, 0))


def test_roundCorners_256():
	"""
	Manual Check
	Desired Output: A circular image 512x512 pixels
	"""
	io.saveImage(OUTPUT + "/test_roundCorners_256.png", effects.roundCorners(IMAGE, 256))


def test_addDropShadowSimple_topLeft():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the top
	left
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowSimple_topLeft.png",
		effects.addDropShadowSimple(IMAGE, [-50, -50]),
	)


def test_addDropShadowSimple_topRight():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the top
	right
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowSimple_topRight.png",
		effects.addDropShadowSimple(IMAGE, [50, -50]),
	)


def test_addDropShadowSimple_bottomLeft():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the bottom
	left
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowSimple_bottomLeft.png",
		effects.addDropShadowSimple(IMAGE, [-50, 50]),
	)


def test_addDropShadowSimple_bottomRight():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the bottom
	right
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowSimple_bottomRight.png",
		effects.addDropShadowSimple(IMAGE, [50, 50]),
	)


# Default: Iterateffectsns 5, Border 50, BG Red, Shadow Black (, Offset 50, 50)
def test_addDropShadowComplex_Iterateffectsns0():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a black blocky shadow to the
	bottom right on a red background
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_Iterateffectsns0.png",
		effects.addDropShadowComplex(IMAGE, 0, 50, [50, 50], "#ff0000", "#000000"),
	)


def test_addDropShadowComplex_Iterateffectsns100():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a black smooth shadow to the
	bottom right on a red background
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_Iterateffectsns100.png",
		effects.addDropShadowComplex(IMAGE, 100, 50, [50, 50], "#ff0000", "#000000"),
	)


def test_addDropShadowComplex_Border0():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels shadow is not smooth at edge
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_Border0.png",
		effects.addDropShadowComplex(IMAGE, 5, 0, [50, 50], "#ff0000", "#000000"),
	)


def test_addDropShadowComplex_Border100():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a red background with some additeffectsnal padding
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_Border100.png",
		effects.addDropShadowComplex(IMAGE, 5, 100, [50, 50], "#ff0000", "#000000"),
	)


def test_addDropShadowComplex_BGBlue():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a blue background
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_BGBlue.png",
		effects.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#0000ff", "#000000"),
	)


def test_addDropShadowComplex_BGGreen():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a green background
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_BGGreen.png",
		effects.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#00ff00", "#000000"),
	)


def test_addDropShadowComplex_ShadowBlue():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a blue shadow to the
	bottom right on a red background
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_ShadowBlue.png",
		effects.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#ff0000", "#0000ff"),
	)


def test_addDropShadowComplex_ShadowGreen():
	"""
	Manual Check
	Desired Output: A square image 512x512 pixels with a green shadow to the
	bottom right on a red background
	"""
	io.saveImage(
		OUTPUT + "/test_addDropShadowComplex_ShadowGreen.png",
		effects.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#ff0000", "#00ff00"),
	)


"""
Manual Check
Desired Output: A circular image 512x512 pixels edges look smooth
"""


def test_roundCornersAntiAlias():
	io.saveImage(
		OUTPUT + "/test_roundCornersAntiAlias.png", effects.roundCornersAntiAlias(IMAGE, 256)
	)


"""
Manual Check
Desired Output: A circular image 512x512 pixels edges look smooth
"""


def test_roundCornersPercentAntiAlias():
	io.saveImage(
		OUTPUT + "/test_roundCornersPercentAntiAlias.png",
		effects.roundCornersAntiAlias(IMAGE, "50%"),
	)


def test_convertBlackAndWhite_background():
	io.saveImage(
		OUTPUT + "/test_convertBlackAndWhite_background.png",
		effects.convertBlackAndWhite(IMAGE, "background"),
	)


def test_convertBlackAndWhite_foreground():
	io.saveImage(
		OUTPUT + "/test_convertBlackAndWhite_foreground.png",
		effects.convertBlackAndWhite(IMAGE, "foreground"),
	)


def test_convertBlackAndWhite_filterLighter():
	io.saveImage(
		OUTPUT + "/test_convertBlackAndWhite_filter-lighter.png",
		effects.convertBlackAndWhite(IMAGE, "filter-lighter"),
	)


def test_convertBlackAndWhite_filterDarker():
	io.saveImage(
		OUTPUT + "/test_convertBlackAndWhite_filter-darker.png",
		effects.convertBlackAndWhite(IMAGE, "filter-darker"),
	)


def test_convertBlackAndWhite_edges():
	io.saveImage(
		OUTPUT + "/test_convertBlackAndWhite_edges.png",
		effects.convertBlackAndWhite(IMAGE, "edges"),
	)


def test_addText_under16():
	io.saveImage(OUTPUT + "/test_addText_under16.png", effects.addText(IMAGE, "01234"))


def test_addText_16():
	io.saveImage(OUTPUT + "/test_addText_16.png", effects.addText(IMAGE, "012345689ABCDEF"))


def test_addText_over16():
	io.saveImage(OUTPUT + "/test_addText_over16.png", effects.addText(IMAGE, "012345689ABCDEFG"))
