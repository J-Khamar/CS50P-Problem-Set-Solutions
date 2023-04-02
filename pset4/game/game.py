from random import randint
from sys import exit

while True:
    try:
        range = int(input("Level: "))
    except ValueError:
        print("Please input a number")
    else:
        if range > 0:
            break
        else:
            print("Please input a positive number")

number = randint(1, range)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        print("Please input a number")
    else:
        if guess > 0:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                exit()
        else:
            print("Please input a positive number")