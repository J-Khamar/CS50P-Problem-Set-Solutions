import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search("^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        for match in matches.groups():
            try:
                match = int(match)
            except ValueError:
                return False
            else:
                if match < 0 or match > 255:
                    return False
                else:
                    pass
        return True
    return False


if __name__ == "__main__":
    main()