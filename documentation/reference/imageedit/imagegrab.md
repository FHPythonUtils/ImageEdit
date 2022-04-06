# Imagegrab

> Auto-generated documentation for [imageedit.imagegrab](../../../imageedit/imagegrab.py) module.

Author FredHappyface 2020...

- [Imageedit](../README.md#imageedit-index) / [Modules](../MODULES.md#imageedit-modules) / [Imageedit](index.md#imageedit) / Imagegrab
    - [doGrabWebpage](#dograbwebpage)
    - [grabWebpage](#grabwebpage)

Uses pyppeteer to leverage a headless version of Chromium

## doGrabWebpage

[[find in source code]](../../../imageedit/imagegrab.py#L14)

```python
async def doGrabWebpage(url, resolution, evalJs):
```

Go to a URL, with a browser with a set resolution and run some js then take a screenshot.

## grabWebpage

[[find in source code]](../../../imageedit/imagegrab.py#L26)

```python
def grabWebpage(
    url: str,
    resolution: tuple[int, int] = (800, 600),
    evalJs=None,
):
```

Take a screenshot of a webpage...

#### Arguments

- `url` *str* - The url of the webpage in question
- `resolution` *(int,int)), optional* - Set the page resolution
- `evalJs` *string* - Javascript to run on the page

#### Returns

- `PIL.Image.Image` - A PIL Image
