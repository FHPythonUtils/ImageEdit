"""imageTrace module creates an svg from a PIL Image. Not particularly
efficient but works ok for this

"""

import operator
from collections import deque
from io import StringIO

from PIL import Image

def addTuple(a, b):
	return tuple(map(operator.add, a, b))

def subTuple(a, b):
	return tuple(map(operator.sub, a, b))

def direction(edge):
	return subTuple(edge[1], edge[0])

def magnitude(a):
	return int(pow(pow(a[0], 2) + pow(a[1], 2), .5))

def normalize(a):
	mag = magnitude(a)
	assert mag > 0, "Cannot normalize a zero-length vector"
	return tuple(map(operator.floordiv, a, [mag]*len(a)))


def svgHeader(width, height):
	"""Generate the svg header

	Args:
		width (int): the width of the SVG
		height (int): the height of the SVG

	Returns:
		string: The svg header
	"""

	return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="%d" height="%d"
	 xmlns="http://www.w3.org/2000/svg" version="1.1">
""" % (width, height)

def joinedEdges(assorted_edges):
	pieces = []
	piece = []
	directions = deque([
		(0, 1),
		(1, 0),
		(0, -1),
		(-1, 0),
		])
	while assorted_edges:
		if not piece:
			piece.append(assorted_edges.pop())
		current_direction = normalize(direction(piece[-1]))
		while current_direction != directions[2]:
			directions.rotate()
		for i in range(1, 4):
			next_end = addTuple(piece[-1][1], directions[i])
			next_edge = (piece[-1][1], next_end)
			if next_edge in assorted_edges:
				assorted_edges.remove(next_edge)
				if i == 2:
					# same direction
					piece[-1] = (piece[-1][0], next_edge[1])
				else:
					piece.append(next_edge)
				if piece[0][0] == piece[-1][1]:
					if normalize(direction(piece[0])) == normalize(direction(piece[-1])):
						piece[-1] = (piece[-1][0], piece.pop(0)[1])
						# same direction
					pieces.append(piece)
					piece = []
				break
		else:
			raise "Failed to find connecting edge"
	return pieces


def doImageToSVG(im, blackAndWhite=False):
	"""_doImage to svg function. Take a PIL Image and some args and return an svg string

	Args:
		im (PIL.Image): A PIL Image to convert to svg
		blackAndWhite (bool, optional): Black and white. Defaults to False.

	Returns:
		string: svg string. Save with file = open(filename, 'w'). then file.write(svg)

	"""
	# collect contiguous pixel groups

	adjacent = ((1, 0), (0, 1), (-1, 0), (0, -1))
	visited = Image.new("1", im.size, 0)

	color_pixel_lists = {}
	print("Collecting Contiguous Pixel Groups\n[", end="")
	count = 0
	width, height = im.size
	for x in range(width):
		if x > (count*width)/78:
			count += 1
			print(".", end="", flush=True)
		for y in range(height):
			here = (x, y)
			if visited.getpixel(here):
				continue
			rgba = im.getpixel((x, y))
			piece = []
			queue = [here]
			visited.putpixel(here, 1)
			while queue:
				here = queue.pop()
				for offset in adjacent:
					neighbour = addTuple(here, offset)
					if not (0 <= neighbour[0] < width) or not (0 <= neighbour[1] < height):
						continue
					if visited.getpixel(neighbour):
						continue
					neighbour_rgba = im.getpixel(neighbour)
					if neighbour_rgba != rgba:
						continue
					queue.append(neighbour)
					visited.putpixel(neighbour, 1)
				piece.append(here)

			if rgba not in color_pixel_lists:
				color_pixel_lists[rgba] = []
			color_pixel_lists[rgba].append(piece)
	print("]")
	del adjacent
	del visited

	# calculate clockwise edges of pixel groups

	edges = {
		(-1, 0):((0, 0), (0, 1)),
		(0, 1):((0, 1), (1, 1)),
		(1, 0):((1, 1), (1, 0)),
		(0, -1):((1, 0), (0, 0)),
		}

	color_edge_lists = {}

	print("Collecting Colour Pixel Lists...")
	color_pixel_lists_items = color_pixel_lists.items()
	color_pixel_lists_len = len(color_pixel_lists_items)
	print("Calculating CLockwise Edges of Pixel Groups\n[", end="")
	count = 0
	x = 0
	for rgba, pieces in color_pixel_lists_items:
		x += 1
		while x/color_pixel_lists_len > count/78:
			count += 1
			print(".", end="", flush=True)
		for piece_pixel_list in pieces:
			edge_set = set([])
			for coord in piece_pixel_list:
				for offset, (start_offset, end_offset) in edges.items():
					neighbour = addTuple(coord, offset)
					start = addTuple(coord, start_offset)
					end = addTuple(coord, end_offset)
					edge = (start, end)
					if neighbour in piece_pixel_list:
						continue
					edge_set.add(edge)
			if rgba not in color_edge_lists:
				color_edge_lists[rgba] = []
			color_edge_lists[rgba].append(edge_set)
	print("]")
	del color_pixel_lists
	del edges

	# join edges of pixel groups

	color_joined_pieces = {}
	print("Collecting Colour Edge Lists...")
	color_edge_lists_items = color_edge_lists.items()
	color_edge_lists_len = len(color_edge_lists_items)
	print("Joining Edges of Pixel Groups\n[", end="")
	count = 0
	x = 0
	for color, pieces in color_edge_lists_items:
		x += 1
		while x/color_edge_lists_len > count/78:
			count += 1
			print(".", end="", flush=True)
		color_joined_pieces[color] = []
		for assorted_edges in pieces:
			color_joined_pieces[color].append(joinedEdges(assorted_edges))
	print("]")
	s = StringIO()
	s.write(svgHeader(*im.size))

	for color, shapes in color_joined_pieces.items():
		for shape in shapes:
			if not blackAndWhite or (blackAndWhite and sum(color[0:3]) < 255):
				s.write(""" <path d=" """)
				for sub_shape in shape:
					here = sub_shape.pop(0)[0]
					s.write(""" M %d,%d """ % here)
					for edge in sub_shape:
						here = edge[0]
						s.write(""" L %d,%d """ % here)
					s.write(""" Z """)
			if blackAndWhite and sum(color[0:3]) < 255:
				s.write("\" />\n")
			elif not blackAndWhite:
				s.write(""" " style="fill:rgb%s; fill-opacity:%.3f; stroke:none;" />\n""" %
				(color[0:3], float(color[3]) / 255))

	s.write("""</svg>\n""")
	return s.getvalue()


def imageToSVG(image, blackAndWhite=False):
	"""Image to svg function. Take a PIL Image and some args and return an svg string

	Args:
		image (PIL.Image): A PIL Image to convert to svg
		blackAndWhite (bool, optional): Black and white. Defaults to False.
		threshold (dict{"darker": bool, "brightness": int}, optional): A threshold
		'object' allowing the user to set instructions for a black and white image.
		If darker is true then only shapes darker than the threshold are added to
		the svg. Brightness is the sum of (r,g,b). Defaults to None.

	Returns:
		string: svg string. Save with file = open(filename, 'w'). then file.write(svg)
	"""
	image = image.quantize(16)
	w, h = image.size
	if w*h > 180*180:
		image = image.resize((180, 180))

	rgbaImage = image.convert('RGBA')

	# Generate SVG
	return doImageToSVG(rgbaImage, blackAndWhite)
