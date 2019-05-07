'''
Author Kieran W 2019-05-07

The add-corners function was not written by me (see below)

Round the corners of an image

'''

from PIL import Image, ImageDraw
import argparse

'''
Function by fraxel: https://stackoverflow.com/users/1175101/fraxel

https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi
'''
def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


'''
Command line arguments. Author Kieran
'''
# Program description
parser = argparse.ArgumentParser(description='Round the corners of an image')
parser.add_argument("-i", "--image", help="specify the path to an input image",
                    action="store")
parser.add_argument("-o", "--output", help="specify the path to an output image",
                    action="store")
parser.add_argument("-r", "--radius", help="specify the corner radius (image w/l /2 for a round image)",
                    action="store")

args = parser.parse_args()


im = Image.open(args.image)
if args.radius is not None:
    im = add_corners(im, int(args.radius))
else:
    im = add_corners(im, int(im.width/2))


if args.output is not None:
    outFileName = args.output
else:
    outFileName = args.image
im.save(outFileName)
