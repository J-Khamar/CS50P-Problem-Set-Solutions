fraction = input("Fraction: ").strip().split("/")

while True:
    try:
        fraction[0] = int(fraction[0])
        fraction[1] = int(fraction[1])
        fraction[0] / fraction[1]
    except (ValueError, ZeroDivisionError):
        fraction = input("Fraction: ").strip().split("/")
    else:
        if fraction[0] <= fraction[1]:
            break
        else:
            fraction = input("Fraction: ").strip().split("/")

percentage = round((fraction[0] / fraction[1]) * 100)

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

