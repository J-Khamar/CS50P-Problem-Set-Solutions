import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search('^<iframe.*src="https?://(www.)?youtube.com/embed/(\w+)".*></iframe>$', s)
    try:
        source = matches.groups()
    except AttributeError:
        return "None"
    else:
        return f"https://youtu.be/{source[1]}"


if __name__ == "__main__":
    main()