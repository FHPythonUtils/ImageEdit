""" Read and write to an .ora image """

import sys
import os
from pathlib import Path
from metprint import Logger, LogType, FHFormatter
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imageedit import io

if len(sys.argv) < 2:
	Logger(FHFormatter()).logPrint("Enter a layered image name for a custom example",
	LogType.WARNING)
	PARENT = str(Path(THISDIR).parent)
	Logger(FHFormatter()).logPrint("Take a look in: \n" + PARENT + "/test/test_readWriteLayered/",
	LogType.INFO)
	layeredImage = io.openLayerImage(PARENT + "/test/test_readWriteLayered/ImageEdit.xcf")
	io.saveImage(PARENT + "/test/test_readWriteLayered/ImageEdit.xcf (export).png",
	layeredImage.getFlattenLayers())
	io.saveLayerImage(PARENT + "/test/test_readWriteLayered/ImageEdit.xcf (export).ora", layeredImage)

else:
	layeredImage = io.openLayerImage(THISDIR + "/input/" + sys.argv[1])
	io.saveImage(THISDIR + "/input/" + sys.argv[1] + " (export).png", layeredImage.getFlattenLayers())
	io.saveLayerImage(THISDIR + "/input/" + sys.argv[1] + " (copy).ora", layeredImage)
