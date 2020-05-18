"""Do a trace of an image on the filesystem using the svgtrace library
"""

import svgtrace


def trace(filename, blackAndWhite=False, mode="default"):
	"""Do a trace of an image on the filesystem using the svgtrace library

	Args:
		filename (string): The location of the file on the filesystem, use an
		absolute filepath for this
		blackAndWhite (bool, optional): Trace a black and white SVG. Defaults to False.
		mode (str, optional): Set the mode. See https://github.com/jankovicsandras/imagetracerjs
		for more information. Defaults to "default".

	Returns:
		str: SVG string
	"""
trace = svgtrace.trace # yapf: disable
