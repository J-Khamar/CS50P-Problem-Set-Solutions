text = input("camelCase: ")

for letter in text:
    if letter.isupper():
        letter = "_" + letter.lower()
    print(letter, end="")
print()



