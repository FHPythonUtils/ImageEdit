'''
Author FredHappyface 20190930

Test imageedit.py with a single 512x512px image. Many of these tests need manual
validation. Look at each test for a brief description of the desired outcome for
each test
'''

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from io import StringIO
from PIL import Image
from imageedit import imageedit

INPUT = THISDIR + "/test_lib_imageEdit/i"
OUTPUT = THISDIR + "/test_lib_imageEdit/o"

IMAGE = imageedit.openImage(INPUT + "/test.png")


def test_logPrint_standard():
	savedStdout = sys.stdout
	try:
		out = StringIO()
		sys.stdout = out
		imageedit.logPrint("test", "standard")
		output = out.getvalue().strip()
		assert output == "test"
	finally:
		sys.stdout = savedStdout

def test_logPrint_success():
	savedStdout = sys.stdout
	try:
		out = StringIO()
		sys.stdout = out
		imageedit.logPrint("test", "success")
		output = out.getvalue().strip()
		assert output == "[\033[92m+ Success\033[00m] test"
	finally:
		sys.stdout = savedStdout

def test_logPrint_warning():
	savedStdout = sys.stdout
	try:
		out = StringIO()
		sys.stdout = out
		imageedit.logPrint("test", "warning")
		output = out.getvalue().strip()
		assert output == "[\033[93m/ Warning\033[00m] test"
	finally:
		sys.stdout = savedStdout

def test_logPrint_error():
	savedStdout = sys.stdout
	try:
		out = StringIO()
		sys.stdout = out
		imageedit.logPrint("test", "error")
		output = out.getvalue().strip()
		assert output == "[\033[91m- Error\033[00m] test"
	finally:
		sys.stdout = savedStdout

def test_logPrint_info():
	savedStdout = sys.stdout
	try:
		out = StringIO()
		sys.stdout = out
		imageedit.logPrint("test", "info")
		output = out.getvalue().strip()
		assert output == "[\033[96m* Info\033[00m] test"
	finally:
		sys.stdout = savedStdout

def test_logPrint_bold():
	savedStdout = sys.stdout
	try:
		out = StringIO()
		sys.stdout = out
		imageedit.logPrint("test", "bold")
		output = out.getvalue().strip()
		assert output == "\033[01mtest\033[00m"
	finally:
		sys.stdout = savedStdout

def test_reduceColours_optimised():
	"""
	Won't be able to see difference but will be able to .getcolors with maxcolors 256
	"""
	assert(not isinstance(imageedit.reduceColours(imageedit.openImage(INPUT + "/test_field.png"), "optimised").getcolors(maxcolors=256), type(None)))

def test_reduceColours_logo():
	"""
	.getcolors with maxcolors 16
	"""
	assert(not isinstance(imageedit.reduceColours(imageedit.openImage(INPUT + "/test_field.png"), "logo").getcolors(maxcolors=16), type(None)))

def test_cropCentre():
	'''
	Manual Check
	Desired Output: A square image 256x256 pixels
	'''
	imageedit.saveImage(OUTPUT+ "/test_cropCentre.png", imageedit.cropCentre(IMAGE, 256, 256))

def test_uncrop():
	'''
	Manual Check
	Desired Output: An 'uncropped' image of a field
	'''
	imageedit.saveImage(OUTPUT + "/test_uncrop.png", imageedit.uncrop(imageedit.openImage(INPUT + "/test_field.png"), 64))

def test_getPixelDimens_px():
	assert(imageedit.getPixelDimens(IMAGE, [256]), [256])

def test_getPixelDimens_scale():
	assert(imageedit.getPixelDimens(IMAGE, ["0.5x"]), [256])

def test_getPixelDimens_percent():
	assert(imageedit.getPixelDimens(IMAGE, ["50%"]), [256])


def test_roundCornersPercent_0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels
	'''
	imageedit.saveImage(OUTPUT+ "/test_roundCornersPercent_0.png", imageedit.roundCorners(IMAGE, "0%"))


def test_roundCornersPercent_50():
	'''
	Manual Check
	Desired Output: A circular image 512x512 pixels
	'''
	imageedit.saveImage(OUTPUT+ "/test_roundCornersPercent_50.png", imageedit.roundCorners(IMAGE, "50%"))


def test_roundCorners_0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels
	'''
	imageedit.saveImage(OUTPUT+ "/test_roundCorners_0.png", imageedit.roundCorners(IMAGE, 0))


def test_roundCorners_256():
	'''
	Manual Check
	Desired Output: A circular image 512x512 pixels
	'''
	imageedit.saveImage(OUTPUT+ "/test_roundCorners_256.png", imageedit.roundCorners(IMAGE, 256))


def test_addDropShadowSimple_topLeft():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the top
	left
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowSimple_topLeft.png", imageedit.addDropShadowSimple(IMAGE, [-50, -50]))


def test_addDropShadowSimple_topRight():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the top
	right
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowSimple_topRight.png", imageedit.addDropShadowSimple(IMAGE, [50, -50]))


def test_addDropShadowSimple_bottomLeft():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the bottom
	left
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowSimple_bottomLeft.png", imageedit.addDropShadowSimple(IMAGE, [-50, 50]))


def test_addDropShadowSimple_bottomRight():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the bottom
	right
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowSimple_bottomRight.png", imageedit.addDropShadowSimple(IMAGE, [50, 50]))


# Default: Iterations 5, Border 50, BG Red, Shadow Black (, Offset 50, 50)
def test_addDropShadowComplex_Iterations0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black blocky shadow to the
	bottom right on a red background
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Iterations0.png", imageedit.addDropShadowComplex(IMAGE, 0, 50, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_Iterations100():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black smooth shadow to the
	bottom right on a red background
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Iterations100.png", imageedit.addDropShadowComplex(IMAGE, 100, 50, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_Border0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels shadow is not smooth at edge
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Border0.png", imageedit.addDropShadowComplex(IMAGE, 5, 0, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_Border100():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a red background with some additional padding
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Border100.png", imageedit.addDropShadowComplex(IMAGE, 5, 100, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_BGBlue():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a blue background
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_BGBlue.png", imageedit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#0000ff", "#000000"))


def test_addDropShadowComplex_BGGreen():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a green background
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_BGGreen.png", imageedit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#00ff00", "#000000"))


def test_addDropShadowComplex_ShadowBlue():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a blue shadow to the
	bottom right on a red background
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_ShadowBlue.png", imageedit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#ff0000", "#0000ff"))


def test_addDropShadowComplex_ShadowGreen():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a green shadow to the
	bottom right on a red background
	'''
	imageedit.saveImage(OUTPUT+ "/test_addDropShadowComplex_ShadowGreen.png", imageedit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#ff0000", "#00ff00"))



def test_resizeImageAbs_256x256():
	assert(imageedit.resizeImage(IMAGE, 256, 256).size == (256, 256))


def test_resizeImageAbs_512x256():
	assert(imageedit.resizeImage(IMAGE, 512, 256).size == (512, 256))


def test_resizeImageAbs_256x512():
	assert(imageedit.resizeImage(IMAGE, 256, 512).size == (256, 512))


def test_resizeImageSquare_1024():
	assert(imageedit.resizeImageSquare(IMAGE, 1024).size == (1024, 1024))


def test_resizeImageSquare_256():
	assert(imageedit.resizeImageSquare(IMAGE, 256).size == (256, 256))


def test_resizeImage_x2():
	assert(imageedit.resizeImageSquare(IMAGE, "2x").size == (1024, 1024))


def test_resizeImage_x0_5():
	assert(imageedit.resizeImageSquare(IMAGE, "0.5x").size == (256, 256))


'''
Manual Check
Desired Output: A circular image 512x512 pixels edges look smooth
'''
def test_roundCornersAntiAlias():
	imageedit.saveImage(OUTPUT+ "/test_roundCornersAntiAlias.png", imageedit.roundCornersAntiAlias(IMAGE, 256))



'''
Manual Check
Desired Output: A circular image 512x512 pixels edges look smooth
'''
def test_roundCornersPercentAntiAlias():
	imageedit.saveImage(OUTPUT+ "/test_roundCornersPercentAntiAlias.png", imageedit.roundCornersAntiAlias(IMAGE, "50%"))



def test_openImagesInDir():
	assert(len(imageedit.openImagesInDir(INPUT + "/*")) == 2)

def test_openImagesInDir_optimised():
	assert(len(imageedit.openImagesInDir(INPUT + "/*")) == 2)


def test_openImage():
	assert(isinstance(imageedit.openImage(INPUT + "/test.png"), Image.Image))

def test_openImage_optimised():
	assert(isinstance(imageedit.openImage(INPUT + "/test.png", "optimised"), Image.Image))


def test_saveImage():
	imageedit.saveImage(OUTPUT + "/test_saveImage_NotOptimised.png", IMAGE, False)
	imageedit.saveImage(OUTPUT + "/test_saveImage_Optimised.png", IMAGE)
	# PNG-24 should be 3x PNG-8 so Optimised = 0.33 * NotOptimised
	# Looks like this doesn't work as well. More like 0.66 * NotOptimised
	NotOptimised = os.path.getsize(OUTPUT + "/test_saveImage_NotOptimised.png")
	Optimised = os.path.getsize(OUTPUT + "/test_saveImage_Optimised.png")
	assert(Optimised < NotOptimised * 0.67)


def test_removeImagePadding_0():
	assert(imageedit.removeImagePadding(IMAGE, 0).size == (512, 512))


def test_removeImagePadding_100():
	assert(imageedit.removeImagePadding(IMAGE, 100).size == (312, 312))


def test_getImageDesc_icon():
	assert(imageedit.getImageDesc(IMAGE) == "icon")


def test_getImageDesc_mask():
	assert(imageedit.getImageDesc(imageedit.resizeImageSquare(IMAGE, 640)) == "mask")


def test_getImageDesc_null():
	assert(imageedit.getImageDesc(imageedit.resizeImageSquare(IMAGE, 256)) == "unknown")


def test_convertBlackAndWhite_background():
	imageedit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_background.png", imageedit.convertBlackAndWhite(IMAGE, "background"))

def test_convertBlackAndWhite_foreground():
	imageedit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_foreground.png", imageedit.convertBlackAndWhite(IMAGE, "foreground"))

def test_convertBlackAndWhite_filterLighter():
	imageedit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_filter-lighter.png", imageedit.convertBlackAndWhite(IMAGE, "filter-lighter"))

def test_convertBlackAndWhite_filterDarker():
	imageedit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_filter-darker.png", imageedit.convertBlackAndWhite(IMAGE, "filter-darker"))

def test_convertBlackAndWhite_edges():
	imageedit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_edges.png", imageedit.convertBlackAndWhite(IMAGE, "edges"))


def test_getSortedColours_none():
	assert(imageedit.getSortedColours(imageedit.openImage(INPUT+ "/test_field.png")) == [(1, (255, 255, 255, 255)), (1, (1, 1, 1, 255))])




def test_addText_under16():
	imageedit.saveImage(OUTPUT+ "/test_addText_under16.png", imageedit.addText(IMAGE, "01234"))

def test_addText_16():
	imageedit.saveImage(OUTPUT+ "/test_addText_16.png", imageedit.addText(IMAGE, "012345689ABCDEF"))


def test_addText_over16():
	imageedit.saveImage(OUTPUT+ "/test_addText_over16.png", imageedit.addText(IMAGE, "012345689ABCDEFG"))
