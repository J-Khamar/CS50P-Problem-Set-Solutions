def main():
    time = input("What time is it? ")
    value = convert(time)

    if value >= 7 and value <= 8:
        print("breakfast time")
    elif value >= 12 and value <= 13:
        print("lunch time")
    elif value >= 18 and value <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    if minutes.endswith("p.m."):
        minutes = int(minutes[0:2])
        hours = int(hours) + 12
    elif minutes.endswith("a.m."):
        minutes = int(minutes[0:2])
    return float(int(hours) + (int(minutes) / 60))



if __name__ == "__main__":
    main()