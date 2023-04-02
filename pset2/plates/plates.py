def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if not (length <= 6 and length >= 2):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    check = 0

    for letter in s:
        if not letter.isalnum():
            return False
        if letter.isdigit():
            check += 1
            if letter == '0' and check == 1:
                return False
        if check > 0 and letter.isalpha() == True:
            return False

    return True


main()