def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    str = ""
    for letter in word:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if letter.lower() not in vowels:
            str = str + letter
    return str


if __name__ == "__main__":
    main()