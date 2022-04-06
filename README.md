[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/ImageEdit.svg?style=for-the-badge)](../../)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/ImageEdit.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/ImageEdit.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/ImageEdit.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/ImageEdit.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/ImageEdit.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/imageedit.svg?style=for-the-badge)](https://pypistats.org/packages/imageedit)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fimageedit)](https://pepy.tech/project/imageedit)
[![PyPI Version](https://img.shields.io/pypi/v/imageedit.svg?style=for-the-badge)](https://pypi.org/project/imageedit)

<!-- omit in toc -->
# ImageEdit

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

[**Now available on pypi.org!**](https://pypi.org/project/imageedit/)

Create various icon masks and shading effects with the imageedit library.
Six example files under main: round.py, makeProjIcons.py, makePWAImages.py,
makeRetro.py, getPWAScreenshots.py and readWriteLayered.py.

Leverages the following libraries to do the heavy lifting:

```none
Pillow
blendmodes
colourswatch
layeredimage
metprint
svgtrace
```

Have a look under test/test_read_write_layered for an example of converting an
xcf to ora and png. Unfortunately, visibility of xcf is currently ignored :(

- [Example Files](#example-files)
- [Comparison to similar solutions](#comparison-to-similar-solutions)
	- [GUI](#gui)
	- [Web](#web)
	- [Advantages of this solution](#advantages-of-this-solution)
	- [Disadvantages of this solution](#disadvantages-of-this-solution)
- [How to use out of the box](#how-to-use-out-of-the-box)
	- [get_pwa_screenshots.py](#get_pwa_screenshotspy)
	- [make_phone_screenshots.py](#make_phone_screenshotspy)
	- [make_proj_icons.py](#make_proj_iconspy)
	- [make_pwa_images.py](#make_pwa_imagespy)
	- [make_retro.py](#make_retropy)
	- [read_write_layered.py](#read_write_layeredpy)
	- [round.py](#roundpy)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Windows - Python.org](#windows---pythonorg)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
	- [Dnf](#dnf)
- [Install Python on MacOS](#install-python-on-macos)
	- [Homebrew](#homebrew)
	- [MacOS - Python.org](#macos---pythonorg)
- [How to run](#how-to-run)
	- [Windows](#windows)
	- [Linux/ MacOS](#linux-macos)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

See the documentation for each library for more information on things you
can use it for.

## Example Files

- get_pwa_screenshots.py
- make_phone_screenshots.py
- make_poj_icons.py
- make_pwa_images.py
- make_retro.py
- read_write_layered.py
- round.py

## Comparison to similar solutions

Similar solutions include but are not limited to:

### GUI

https://www.getpaint.net/

### Web

https://realfavicongenerator.net/

### Advantages of this solution

- Lightweight: few dependencies required (python, pillow, blendmodes,
layeredimage, and svgtrace)
- Quick: when given a regular or mask image it can produce many
variants in a relatively short amount of time
- Customizable: write your own scripts to leverage imageEdit (python knowledge
required)
- Produce a PWA mask icon out of the box
- SVG tracing lib doesn't require potrace/ pypotrace which can be challenging to
set up on Windows
- SVG tracing using imageTracerJs.py (https://github.com/jankovicsandras/imagetracerjs)
is pretty good (requires pyppeteer: https://github.com/miyakogi/pyppeteer)

### Disadvantages of this solution

- Specific image dimensions needed out of the box: whilst this is something that
could be changed, maskable icons are 640x640 and regular icons are 512x512

## How to use out of the box

### get_pwa_screenshots.py

### make_phone_screenshots.py

### make_proj_icons.py

### make_pwa_images.py

1. Put regular 512x512 image or mask 640x640 image under main/input in this
example I am using lightfox.png

	<img src="readme-assets/examples/lightfox.png" alt="LightFox" width="128">

2. Run ```make_pwa_images.py``` and navigate to main/output/lightfox.png/pwa

	<div>
	<img src="readme-assets/examples/mask.png" alt="LightFox" width="128">
	<img src="readme-assets/examples/round-192.png" alt="LightFox" width="38">
	<img src="readme-assets/examples/round-512.png" alt="LightFox" width="102">
	<img src="readme-assets/examples/square-180.png" alt="LightFox" width="36">
	<img src="readme-assets/examples/squircle-256.png" alt="LightFox" width="52">
	</div>

### make_retro.py

1. Put regular 512x512 image or mask 640x640 image under main/input. In this
   example I am using BlendModes.png

	<img src="readme-assets/examples/blendmodes.png" alt="BlendModes" width="128">

2. Run ```make_retro.py``` and navigate to main/output/blendmodes.png/retro
	Personal Computers

	<div>
	<img src="readme-assets/examples/3level.png" alt="BlendModes" width="128">
	<img src="readme-assets/examples/bbc-micro.png" alt="BlendModes" width="128">
	<img src="readme-assets/examples/zxspectrum.png" alt="BlendModes" width="128">
	<img src="readme-assets/examples/websafe.png" alt="BlendModes" width="128">
	</div>

	Mobile Operating Systems

	iOS

	<div>
	<img src="readme-assets/examples/ios1.png" alt="BlendModes" width="128">
	<img src="readme-assets/examples/ios7.png" alt="BlendModes" width="128">
	</div>

	Android

	<div>
	<img src="readme-assets/examples/android2.png" alt="BlendModes" width="128">
	<img src="readme-assets/examples/android6.png" alt="BlendModes" width="128">
	<img src="readme-assets/examples/android7.png" alt="BlendModes" width="128">
	<img src="readme-assets/examples/android8.png" alt="BlendModes" width="128">
	</div>

### read_write_layered.py

### round.py

## Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

<!--
- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
-->
- The [Technical Reference](/documentation/reference) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software.
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Install With PIP

```python
pip install imageedit
```

Head to https://pypi.org/project/imageedit/ for more info

## Language information

### Built for

This program has been written for Python versions 3.7 - 3.10 and has been tested with both 3.7 and
3.10

## Install Python on Windows

### Chocolatey

```powershell
choco install python
```

### Windows - Python.org

To install Python, go to https://www.python.org/downloads/windows/ and download the latest
version.

## Install Python on Linux

### Apt

```bash
sudo apt install python3.x
```

### Dnf

```bash
sudo dnf install python3.x
```

## Install Python on MacOS

### Homebrew

```bash
brew install python@3.x
```

### MacOS - Python.org

To install Python, go to https://www.python.org/downloads/macos/ and download the latest
version.

## How to run

### Windows

- Module
	`py -3.x -m [module]` or `[module]` (if module installs a script)

- File
	`py -3.x [file]` or `./[file]`

### Linux/ MacOS

- Module
	`python3.x -m [module]` or `[module]` (if module installs a script)

- File
	`python3.x [file]` or `./[file]`

## Download Project

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to clone to
4. Type 'git clone' followed by URL in step 2
	```bash
	git clone https://github.com/FHPythonUtils/ImageEdit
	```

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files

### Licence

MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog

See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale

The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
