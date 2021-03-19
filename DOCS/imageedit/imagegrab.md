# imagegrab

> Auto-generated documentation for [imageedit.imagegrab](../../imageedit/imagegrab.py) module.

Author FredHappyface 2020
Uses pyppeteer to leverage a headless version of Chromium

- [Imageedit](../README.md#imageedit-index) / [Modules](../README.md#imageedit-modules) / [imageedit](index.md#imageedit) / imagegrab
    - [doGrabWebpage](#dograbwebpage)
    - [grabWebpage](#grabwebpage)

## doGrabWebpage

[[find in source code]](../../imageedit/imagegrab.py#L12)

```python
async def doGrabWebpage(url, resolution, evalJs):
```

 Go to a URL, with a browser with a set resolution and run some js
then take a screenshot

## grabWebpage

[[find in source code]](../../imageedit/imagegrab.py#L26)

```python
def grabWebpage(url, resolution=(800, 600), evalJs=None):
```

Take a screenshot of a webpage

#### Arguments

- `url` *string* - The url of the webpage in question
- `resolution` *(int,int)), optional* - Set the page resolution
- `evalJs` *string* - Javascript to run on the page

#### Returns

- `PIL.Image.Image` - A PIL Image
