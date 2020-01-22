#!/usr/bin/env python3
'''
Author FredHappyface 20190918

Grab some screenshots for my pwas - obviously, you can set these to your own
urls and set your own scripts
'''

import os, sys
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR) + "/lib")
import imageGrab, imageEdit

if __name__ == "__main__": # pragma: no cover

	outputDir = THISDIR + "/output/pwascreenshots/"

	baseUrl = "https://fredhappyface.github.io/"
	projects = {
		"PWA.Home/": ["index.html", "info.html", "settings.html"],
		"PWA.BlackC4t/": ["2kotp.html", "index.html", "password.html", "public.html"],
		"PWA.Brainf/": ["index.html"],
		"PWA.HappyShibe/": ["index.html"],
	}

	scripts = [
	"document.getElementById('theme').innerHTML = '<link rel=\"stylesheet\" href=\"https://fredhappyface.github.io/css/theme/light.css\" id=\"theme\">'",
	"document.getElementById('theme').innerHTML = '<link rel=\"stylesheet\" href=\"https://fredhappyface.github.io/css/theme/dark.css\" id=\"theme\">'",
	"document.getElementById('theme').innerHTML = '<link rel=\"stylesheet\" href=\"https://fredhappyface.github.io/css/theme/black.css\" id=\"theme\">'",
	]


	for project in projects:
		pages = projects[project]
		for index, script in enumerate(scripts):
			imageEdit.saveImage(outputDir+project+"themes/theme-"+str(index)+".png", imageEdit.resizeImage(imageGrab.grabWebpage(baseUrl+project+pages[0], (375, 667), evalJs=script), "2x", "2x"))
		for index, page in enumerate(pages):
			imageEdit.saveImage(outputDir+project+"mobile/screenshot-"+str(index)+".png", imageEdit.resizeImage(imageGrab.grabWebpage(baseUrl+project+page, (375, 667), evalJs=scripts[0]), "2x", "2x"))
			imageEdit.saveImage(outputDir+project+"desktop/screenshot-"+str(index)+".png", imageGrab.grabWebpage(baseUrl+project+page, (1920, 1080), evalJs=scripts[0]))
