# Imagegrab

[Imageedit Index](../README.md#imageedit-index) / [Imageedit](./index.md#imageedit) / Imagegrab

> Auto-generated documentation for [imageedit.imagegrab](../../../imageedit/imagegrab.py) module.

- [Imagegrab](#imagegrab)
  - [grabWebpage](#grabwebpage)

## grabWebpage

[Show source in imagegrab.py:15](../../../imageedit/imagegrab.py#L15)

Take a screenshot of a webpage

#### Arguments

----
 - `url` *str* - The url of the webpage in question
 - `resolution` *(int,int)), optional* - Set the page resolution
 - `evalJs` *string* - Javascript to run on the page

#### Returns

-------
 - `PIL.Image.Image` - A PIL Image

#### Signature

```python
def grabWebpage(url: str, resolution: tuple[int, int] = (800, 600), evalJs=None): ...
```