from sys import argv, exit
from os.path import splitext
from PIL import Image, ImageOps

if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")

extensions = [".jpg", ".jpeg", ".png"]

ext1 = splitext(argv[1])
ext2 = splitext(argv[2])

if ext1[1] not in extensions or ext2[1] not in extensions:
    exit("Invalid output")

if ext1[1] != ext2[1]:
    exit("Input and output have different extensions")

try:
    before = Image.open(argv[1])
except FileNotFoundError:
    exit("Input does not exist")
else:
    pass

shirt = Image.open("shirt.png")
before = ImageOps.fit(before, shirt.size)
before.paste(shirt, shirt)
before.save(argv[2])