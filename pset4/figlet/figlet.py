from sys import argv, exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
font_list = figlet.getFonts()

if len(argv) == 1:
    text = input("Input: ")
    font_choice = choice(font_list)
    figlet.setFont(font=font_choice)
    print(figlet.renderText(text))
elif len(argv) == 3:
    if (argv[1] == "-f" or argv[1] == "--font") and (argv[2] in font_list):
        text = input("Input: ")
        figlet.setFont(font=argv[2])
        print(figlet.renderText(text))
    else:
        exit("Invalid usage")
else:
    exit("Invalid usage")