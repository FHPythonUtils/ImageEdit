#!/usr/bin/env python3
'''
Author FredHappyface 20190918

Grab some screenshots for my pwas - obviously, you can set these to your own
urls and set your own scripts
'''

import sys
import os
from pathlib import Path
from metprint import Logger, LogType, FHFormatter
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imageedit import io, transform, imagegrab

if __name__ == "__main__": # pragma: no cover

	outputDir = THISDIR + "/output/pwascreenshots/"

	baseUrl = "https://fredhappyface.com/"
	projects = {
	"home/": ["index.html", "info.html", "settings.html"],
	"blackc4t/": ["2kotp.html", "index.html", "password.html", "public.html"],
	"brainf/": ["index.html"],
	"happyshibe/": ["index.html"],
	"passwordgen/": ["index.html", "advanced.html"], }

	scripts = [
	"const rootStylesAuto = document.styleSheets[0].cssRules[0].style; const darkStylesAuto = document.styleSheets[0].cssRules[1].cssRules[0].style; rootStylesAuto.setProperty(\"--var-c-primary\", \"#FAFAFA\"); rootStylesAuto.setProperty(\"--var-c-secondary\", \"#EAEAEB\"); rootStylesAuto.setProperty(\"--var-c-text\", \"#383A42\"); darkStylesAuto.setProperty(\"--var-c-primary\", \"#FAFAFA\"); darkStylesAuto.setProperty(\"--var-c-secondary\", \"#EAEAEB\"); darkStylesAuto.setProperty(\"--var-c-text\", \"#383A42\"); rootStylesAuto.setProperty(\"--var-c-black\", \"0\")",
	"const rootStylesAuto = document.styleSheets[0].cssRules[0].style; const darkStylesAuto = document.styleSheets[0].cssRules[1].cssRules[0].style; rootStylesAuto.setProperty(\"--var-c-primary\", \"#181A1F\"); rootStylesAuto.setProperty(\"--var-c-secondary\", \"#282C34\"); rootStylesAuto.setProperty(\"--var-c-text\", \"#ABB2BF\"); darkStylesAuto.setProperty(\"--var-c-primary\", \"#181A1F\"); darkStylesAuto.setProperty(\"--var-c-secondary\", \"#282C34\"); darkStylesAuto.setProperty(\"--var-c-text\", \"#ABB2BF\"); rootStylesAuto.setProperty(\"--var-c-black\", \"0\")",
	"const rootStylesAuto = document.styleSheets[0].cssRules[0].style; const darkStylesAuto = document.styleSheets[0].cssRules[1].cssRules[0].style; rootStylesAuto.setProperty(\"--var-c-primary\", \"#000000\"); rootStylesAuto.setProperty(\"--var-c-secondary\", \"#000000\"); rootStylesAuto.setProperty(\"--var-c-text\", \"#ABB2BF\"); darkStylesAuto.setProperty(\"--var-c-primary\", \"#181A1F\"); darkStylesAuto.setProperty(\"--var-c-secondary\", \"#282C34\"); darkStylesAuto.setProperty(\"--var-c-text\", \"#ABB2BF\"); rootStylesAuto.setProperty(\"--var-c-black\", \"1\")"
	]

	for project in projects:
		Logger(FHFormatter()).logPrint(project, LogType.INFO)
		pages = projects[project]
		for index, script in enumerate(scripts):
			io.saveImage(
			outputDir + project + "themes/theme-" + str(index) + ".png",
			transform.resize(
			imagegrab.grabWebpage(baseUrl + project + pages[0], (375, 667), evalJs=script), "2x",
			"2x"))
		for index, page in enumerate(pages):
			io.saveImage(
			outputDir + project + "mobile/screenshot-" + str(index) + ".png",
			transform.resize(
			imagegrab.grabWebpage(baseUrl + project + page, (375, 667), evalJs=scripts[0]), "2x",
			"2x"))
			io.saveImage(
			outputDir + project + "desktop/screenshot-" + str(index) + ".png",
			imagegrab.grabWebpage(baseUrl + project + page, (1920, 1080), evalJs=scripts[0]))
