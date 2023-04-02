import random


def get_int(text):
    while True:
        try:
            number = int(input(text))
        except ValueError:
            pass
        else:
            break
    return number


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for j in range(3):
            print(f"{x} + {y} = ", end="")
            answer = get_int("")
            if answer != (x + y):
                print("EEE")
            else:
                score += 1
                break
            if j == 2:
                print(x + y)
    print(score)


def get_level():
    while True:
        level = get_int("Level: ")
        if level in [1, 2, 3]:
            break
    return level


# This is a comment
def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    else:
        number = random.randint(100, 999)
    return number


if __name__ == "__main__":
    main()