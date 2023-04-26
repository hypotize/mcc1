from PIL import Image
import sys

def diff(color1, color2):
	diffR = color1[0] - color2[0]
	diffG = color1[1] - color2[1]
	diffB = color1[2] - color2[2]
	return diffR * diffR + diffG * diffG + diffB * diffB

if len(sys.argv) == 4:
	infile = sys.argv[1]
	outfile = sys.argv[2]
	thresh = int(sys.argv[3])
elif len(sys.argv) == 3:
	infile = sys.argv[1]
	outfile = sys.argv[2]
	thresh = 0
else:
	print("usage; python3 transparent.py infile outfile (thresh)")
	sys.exit(0)
	
img = Image.open(infile)
img = img.convert('RGBA')
que = [(0,0)]

while len(que) > 0:
	x, y = que.pop(0)
	color = img.getpixel((x, y))
	for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
		nx, ny = x + dx, y + dy
		if 0 <= nx < img.size[0] and 0 <= ny < img.size[1]:
			ncolor = img.getpixel((nx, ny))
			if ncolor[3] == 255 and diff(color, ncolor) <= thresh:
				ncolor = (ncolor[0], ncolor[1], ncolor[2], 0)
				img.putpixel((nx, ny), ncolor)
				que.append((nx, ny))	

img.save(outfile)
