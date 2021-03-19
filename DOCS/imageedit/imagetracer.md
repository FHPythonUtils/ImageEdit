# imagetracer

> Auto-generated documentation for [imageedit.imagetracer](../../imageedit/imagetracer.py) module.

Do a trace of an image on the filesystem using the svgtrace library

- [Imageedit](../README.md#imageedit-index) / [Modules](../README.md#imageedit-modules) / [imageedit](index.md#imageedit) / imagetracer
    - [trace](#trace)

## trace

[[find in source code]](../../imageedit/imagetracer.py#L7)

```python
def trace(filename, blackAndWhite=False, mode='default'):
```

Do a trace of an image on the filesystem using the svgtrace library

#### Arguments

- `filename` *string* - The location of the file on the filesystem, use an
absolute filepath for this
- `blackAndWhite` *bool, optional* - Trace a black and white SVG. Defaults to False.
- `mode` *str, optional* - Set the mode. See https://github.com/jankovicsandras/imagetracerjs
for more information. Defaults to "default".

#### Returns

- `str` - SVG string
