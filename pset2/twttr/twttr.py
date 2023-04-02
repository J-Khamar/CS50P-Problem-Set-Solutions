text = input("Input: ")

for letter in text:
    vowels = ['a', 'e', 'i', 'o', 'u']
    if not letter.lower() in vowels:
        print(letter, end="")
print()
