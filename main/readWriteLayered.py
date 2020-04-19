""" Read and write to an .ora image """

import sys
import os
from pathlib import Path
from metprint import Logger, LogType, FHFormatter
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imageedit import io

if len(sys.argv) < 2:
	Logger(FHFormatter()).logPrint("Enter a layered image name", LogType.ERROR)

layeredImage = io.openLayerImage(THISDIR + "/input/" + sys.argv[1])
io.saveImage(THISDIR + "/input/" + sys.argv[1] + " (export).png", layeredImage.getFlattenLayers())
io.saveLayerImage(THISDIR + "/input/" + sys.argv[1] + " (copy).ora", layeredImage)
