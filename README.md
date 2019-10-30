
<p float="left">
<img src="https://img.shields.io/github/languages/top/fredhappyface/Python.ImageRound.svg?style=flat-square" alt="Github top language">
<img src="https://img.shields.io/codacy/grade/:codacy-proj-id:.svg?style=flat-square" alt="Codacy grade">
<img src="https://img.shields.io/codacy/coverage/:codacy-proj-id:.svg?style=flat-square" alt="Codacy coverage">
<img src="https://img.shields.io/github/repo-size/fredhappyface/Python.ImageRound.svg?style=flat-square" alt="Repository size">
<img src="https://img.shields.io/github/issues/fredhappyface/Python.ImageRound.svg?style=flat-square" alt="Issues">
<img src="https://img.shields.io/github/license/fredhappyface/Python.ImageRound.svg?style=flat-square" alt="License">
<img src="https://img.shields.io/github/commit-activity/m/fredhappyface/Python.ImageRound.svg?style=flat-square" alt="Commit activity">
<img src="https://img.shields.io/github/last-commit/fredhappyface/Python.ImageRound.svg?style=flat-square" alt="Last commit">
</p>


# Python.ImageRound


<img src="readme-assets/icons/proj-icon.png" alt="Project Icon" width="100">

No longer just rounds the corners of an image. Create various icon masks and
shading effects with the imageEdit library. Three example files: round.py,
makeProjIcons and makePWAImages.

## Comparison to similar solutions

Similar solutions include but are not limited to:

### GUI
https://www.getpaint.net/

### Web
https://realfavicongenerator.net/

### Advantages of this solution
- Minimal: few dependencies required (python and pillow)
- Quick: when given a regular or mask image it can produce a large number or
variants in a relatively short amount of time
- Customisable: write your own scripts to leverage imageEdit (python knowledge
required)
- Produce a PWA mask icon out of the box

### Disadvantages of this solution
- No SVG tracing: something that I would like to add
- Specific image dimensions needed out of the box: whilst this is something that
could be changed, maskable icons are 640x640 and regular icons are 512x512

## How to use out of the box (makePWAImages)

1. Put regular 512x512 image or mask 640x640 image under main/input in this
example I am using lightfox.png

<img src="readme-assets/examples/lightfox.png" alt="LightFox" width="128">

2. Run ```makePWAImages.py``` and navigate to main/output/lightfox.png/pwa

<img src="readme-assets/examples/mask.png" alt="LightFox" width="128">
<img src="readme-assets/examples/round-192.png" alt="LightFox" width="38">
<img src="readme-assets/examples/round-512.png" alt="LightFox" width="102">
<img src="readme-assets/examples/square-180.png" alt="LightFox" width="36">
<img src="readme-assets/examples/squircle-256.png" alt="LightFox" width="52">


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/[user-name]/[repository]
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8 <https://www.python.org/downloads/release/python-380/>
on a Windows 10 PC.
### Other versions
To install Python, go to <https://www.python.org/> and download the latest
version.
## How to run
1. Open the .py file in IDLE or vscode
2. Run by pressing F5 or by selecting Run> Run Module


## Licence
MIT License
Copyright (c) fredhappyface
(See the [LICENSE](/LICENSE.md) for more information.)


<!--
TODO: Add screenshots to readme-assets/screenshots/desktop/ named
screenshot-[number].png
-->
## Screenshots

### Desktop
|Screenshots                                                                                  |
|:-:                                                                                          |
|<img src="readme-assets/screenshots/desktop/screenshot-1.png" alt="Screenshot 1" width="600">|
|<img src="readme-assets/screenshots/desktop/screenshot-2.png" alt="Screenshot 2" width="600">|
|<img src="readme-assets/screenshots/desktop/screenshot-3.png" alt="Screenshot 3" width="600">|



## Limited Support
Expect this project to be supported for approximately 6 months (for bug-fixes
only). Note that this is not guaranteed. Create an issue for bugs (as this
project is carried out in spare time, you may have to wait for a few days)

<img src="readme-assets/support/partial.png" alt="Limited Support" width="600">
