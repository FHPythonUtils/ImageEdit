"""
Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium
"""
import asyncio
from os import remove
from pyppeteer import launch
from PIL import Image
from metprint import LogType, Logger, FHFormatter


async def doGrabWebpage(url, resolution, evalJs):
	''' Go to a URL, with a browser with a set resolution and run some js
	then take a screenshot'''
	browser = await launch(
	options={'args': ['--no-sandbox', '--disable-web-security']})
	page = await browser.newPage()
	await page.setViewport({"width": resolution[0], "height": resolution[1]})
	await page.goto(url)
	if evalJs is not None:
		await page.evaluate(evalJs)
	await page.screenshot({'path': 'temp.png'})
	await browser.close()


def grabWebpage(url, resolution=(800, 600), evalJs=None):
	"""Take a screenshot of a webpage

	Args:
		url (string): The url of the webpage in question
		resolution ((int,int)), optional): Set the page resolution
		evalJs (string): Javascript to run on the page

	Returns:
		PIL.Image.Image: A PIL Image
	"""
	asyncio.get_event_loop(
	).run_until_complete(doGrabWebpage(url, resolution, evalJs))
	image = Image.open("temp.png")
	try:
		remove("temp.png")
	except PermissionError:
		Logger(FHFormatter()).logPrint(
		"Unable to clean up, manually " +
		"remove temp.png from project root or ignore", LogType.WARNING)
	return image
