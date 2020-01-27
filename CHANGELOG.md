# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2020.2 - 2020/01/27
- Removed function **createDirsIfRequired** from imageEdit.py and replaced with
  a one-liner that does the same thing

## 2020.1 - 2020/01/22
- Removed imageTrace.py as it was slow and I honestly don't see why anyone
  would use it over imageTracerJs.py
- Added imageGrab.py
- Added Docs.md for library documentation
- Updated README
- Tidied up libraries and scripts

## Add New functions to imageEdit.py - 2020/01/13
```python
logPrint(printText, printType="standard"):
reduceColours(image, mode="optimised"):
cropCentre(image, width, height):
uncrop(image, padding):
getPixelDimens(image, dimens):
```

## Add Changelog (overdue) - 2020/01/13
- Add a changelog to the project that is rather overdue
- Lib consists of the following files:
	- FiraCode-Light.ttf
	- imageEdit.py
	- imageTrace.py
	- imagetracer.html
	- imagetracer.js
	- imageTracerJs.py
