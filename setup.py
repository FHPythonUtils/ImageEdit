"""Do setup for uploading to pypi
"""
import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="imageedit",
	version="2020.3",
	author="FredHappyface",
	description="Create various icon masks and shading effects with the imageedit library",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/FredHappyface/Python.ImageEdit",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.0',
)
