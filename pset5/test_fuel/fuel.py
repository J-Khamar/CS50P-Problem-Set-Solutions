def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    fraction = fraction.split("/")
    fraction[0] = int(fraction[0])
    fraction[1] = int(fraction[1])
    if fraction[1] == 0:
        raise ZeroDivisionError
    if fraction[0] > fraction[1]:
            raise ValueError

    return round((fraction[0] / fraction[1]) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()