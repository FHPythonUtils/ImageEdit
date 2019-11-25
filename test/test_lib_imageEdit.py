'''
Author FredHappyface 20190930

Test imageEdit.py with a single 512x512px image. Many of these tests need manual
validation. Look at each test for a brief description of the deired outcome for
each test
'''

import os, sys, inspect
THISDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, os.path.dirname(THISDIR) + "/lib")

import imageEdit
from PIL import Image

INPUT = THISDIR + "/test_lib_imageEdit/i"
OUTPUT = THISDIR + "/test_lib_imageEdit/o"

IMAGE = imageEdit.openImage(INPUT + "/test.png")


def test_roundCornersPercent_0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels
	'''
	imageEdit.saveImage(OUTPUT+ "/test_roundCornersPercent_0.png", imageEdit.roundCornersPercent(IMAGE, 0))


def test_roundCornersPercent_50():
	'''
	Manual Check
	Desired Output: A circular image 512x512 pixels
	'''
	imageEdit.saveImage(OUTPUT+ "/test_roundCornersPercent_50.png", imageEdit.roundCornersPercent(IMAGE, 50))


def test_roundCorners_0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels
	'''
	imageEdit.saveImage(OUTPUT+ "/test_roundCorners_0.png", imageEdit.roundCorners(IMAGE, 0))


def test_roundCorners_256():
	'''
	Manual Check
	Desired Output: A circular image 512x512 pixels
	'''
	imageEdit.saveImage(OUTPUT+ "/test_roundCorners_256.png", imageEdit.roundCorners(IMAGE, 256))


def test_addDropShadowSimple_topLeft():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the top
	left
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowSimple_topLeft.png", imageEdit.addDropShadowSimple(IMAGE, [-50, -50]))


def test_addDropShadowSimple_topRight():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the top
	right
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowSimple_topRight.png", imageEdit.addDropShadowSimple(IMAGE, [50, -50]))


def test_addDropShadowSimple_bottomLeft():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the bottom
	left
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowSimple_bottomLeft.png", imageEdit.addDropShadowSimple(IMAGE, [-50, 50]))


def test_addDropShadowSimple_bottomRight():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a shadow 50 px to the bottom
	right
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowSimple_bottomRight.png", imageEdit.addDropShadowSimple(IMAGE, [50, 50]))


# Default: Iterations 5, Border 50, BG Red, Shadow Black (, Offset 50, 50)
def test_addDropShadowComplex_Iterations0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black blocky shadow to the
	bottom right on a red background
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Iterations0.png", imageEdit.addDropShadowComplex(IMAGE, 0, 50, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_Iterations100():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black smooth shadow to the
	bottom right on a red background
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Iterations100.png", imageEdit.addDropShadowComplex(IMAGE, 100, 50, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_Border0():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels shadow is not smooth at edge
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Border0.png", imageEdit.addDropShadowComplex(IMAGE, 5, 0, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_Border100():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a red background with some additional padding
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_Border100.png", imageEdit.addDropShadowComplex(IMAGE, 5, 100, [50, 50], "#ff0000", "#000000"))


def test_addDropShadowComplex_BGBlue():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a blue background
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_BGBlue.png", imageEdit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#0000ff", "#000000"))


def test_addDropShadowComplex_BGGreen():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a black shadow to the
	bottom right on a green background
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_BGGreen.png", imageEdit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#00ff00", "#000000"))


def test_addDropShadowComplex_ShadowBlue():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a blue shadow to the
	bottom right on a red background
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_ShadowBlue.png", imageEdit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#ff0000", "#0000ff"))


def test_addDropShadowComplex_ShadowGreen():
	'''
	Manual Check
	Desired Output: A square image 512x512 pixels with a green shadow to the
	bottom right on a red background
	'''
	imageEdit.saveImage(OUTPUT+ "/test_addDropShadowComplex_ShadowGreen.png", imageEdit.addDropShadowComplex(IMAGE, 5, 50, [50, 50], "#ff0000", "#00ff00"))



def test_resizeImageAbs_256x256():
	assert(imageEdit.resizeImageAbs(IMAGE, 256, 256).size == (256, 256))


def test_resizeImageAbs_512x256():
	assert(imageEdit.resizeImageAbs(IMAGE, 512, 256).size == (512, 256))


def test_resizeImageAbs_256x512():
	assert(imageEdit.resizeImageAbs(IMAGE, 256, 512).size == (256, 512))


def test_resizeImageSquare_1024():
	assert(imageEdit.resizeImageSquare(IMAGE, 1024).size == (1024, 1024))


def test_resizeImageSquare_256():
	assert(imageEdit.resizeImageSquare(IMAGE, 256).size == (256, 256))


def test_resizeImage_x2():
	assert(imageEdit.resizeImage(IMAGE, 2).size == (1024, 1024))


def test_resizeImage_x0_5():
	assert(imageEdit.resizeImage(IMAGE, 0.5).size == (256, 256))


'''
Manual Check
Desired Output: A circular image 512x512 pixels edges look smooth
'''
def test_roundCornersAntiAlias():
	imageEdit.saveImage(OUTPUT+ "/test_roundCornersAntiAlias.png", imageEdit.roundCornersAntiAlias(IMAGE, 256))



'''
Manual Check
Desired Output: A circular image 512x512 pixels edges look smooth
'''
def test_roundCornersPercentAntiAlias():
	imageEdit.saveImage(OUTPUT+ "/test_roundCornersPercentAntiAlias.png", imageEdit.roundCornersPercentAntiAlias(IMAGE, 50))



def test_openImagesInDir():
	assert(len(imageEdit.openImagesInDir(INPUT + "/*")) == 2)


def test_openImage():
	assert(isinstance(imageEdit.openImage(INPUT + "/test.png"), Image.Image))


def test_saveImage():
	imageEdit.saveImage(OUTPUT + "/test_saveImage_NotOptimised.png", IMAGE, False)
	imageEdit.saveImage(OUTPUT + "/test_saveImage_Optimised.png", IMAGE)
	# PNG-24 should be 3x PNG-8 so Optimised = 0.33 * NotOptimised
	# Looks like this doesn't work as well. More like 0.66 * NotOptimised
	NotOptimised = os.path.getsize(OUTPUT + "/test_saveImage_NotOptimised.png")
	Optimised = os.path.getsize(OUTPUT + "/test_saveImage_Optimised.png")
	assert(Optimised < NotOptimised * 0.67)


def test_createDirsIfRequired():
	imageEdit.createDirsIfRequired(OUTPUT + "/newdir/test_createDirsIfRequired")
	assert(os.path.isdir(OUTPUT + "/newdir"))


def test_removeImagePadding_0():
	assert(imageEdit.removeImagePadding(IMAGE, 0).size == (512, 512))


def test_removeImagePadding_100():
	assert(imageEdit.removeImagePadding(IMAGE, 100).size == (312, 312))


def test_getImageDesc_icon():
	assert(imageEdit.getImageDesc(IMAGE) == "icon")


def test_getImageDesc_mask():
	assert(imageEdit.getImageDesc(imageEdit.resizeImageSquare(IMAGE, 640)) == "mask")


def test_getImageDesc_null():
	assert(isinstance(imageEdit.getImageDesc(imageEdit.resizeImageSquare(IMAGE, 256)), type(None)))


def test_convertBlackAndWhite_background():
	imageEdit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_background.png", imageEdit.convertBlackAndWhite(IMAGE, "background"))

def test_convertBlackAndWhite_foreground():
	imageEdit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_foreground.png", imageEdit.convertBlackAndWhite(IMAGE, "foreground"))

def test_convertBlackAndWhite_filterLighter():
	imageEdit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_filter-lighter.png", imageEdit.convertBlackAndWhite(IMAGE, "filter-lighter"))

def test_convertBlackAndWhite_filterDarker():
	imageEdit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_filter-darker.png", imageEdit.convertBlackAndWhite(IMAGE, "filter-darker"))

def test_convertBlackAndWhite_edges():
	imageEdit.saveImage(OUTPUT+ "/test_convertBlackAndWhite_edges.png", imageEdit.convertBlackAndWhite(IMAGE, "edges"))


def test_addText_under16():
	imageEdit.saveImage(OUTPUT+ "/test_addText_under16.png", imageEdit.addText(IMAGE, "01234"))

def test_addText_16():
	imageEdit.saveImage(OUTPUT+ "/test_addText_16.png", imageEdit.addText(IMAGE, "012345689ABCDEF"))


def test_addText_over16():
	imageEdit.saveImage(OUTPUT+ "/test_addText_over16.png", imageEdit.addText(IMAGE, "012345689ABCDEFG"))
