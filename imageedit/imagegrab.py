"""Author FredHappyface.

Uses playwright to leverage a headless version of Chromium
"""

from __future__ import annotations

import os

from install_playwright import install
from PIL import Image
from playwright.sync_api import sync_playwright


def grabWebpage(url: str, resolution: tuple[int, int] = (800, 600), evalJs=None):
	"""Take a screenshot of a webpage.

	Args:
	----
		url (str): The url of the webpage in question
		resolution ((int,int)), optional): Set the page resolution
		evalJs (string): Javascript to run on the page

	Returns:
	-------
		PIL.Image.Image: A PIL Image

	"""
	with sync_playwright() as p:
		install(p.chromium)
		browser = p.chromium.launch()

		page = browser.new_page()
		page.set_viewport_size({"width": resolution[0], "height": resolution[1]})
		page.goto(url)
		if evalJs is not None:
			page.evaluate(evalJs)
		page.screenshot(path="temp.png")
		browser.close()

	image = Image.open("temp.png")
	try:
		os.remove("temp.png")
	except PermissionError:
		print("WARNING: Unable to clean up, manually remove temp.png from project root or ignore")
	return image
