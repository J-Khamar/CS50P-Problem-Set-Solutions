import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search("(\d?\d):?(\d\d)? (AM|PM) to (\d?\d):?(\d\d)? (AM|PM)", s)
    if matches:
        times = list(matches.groups())
    else:
        raise ValueError

    new_times = []
    for time in times:
        if time == None:
            new_times.append(0)
        elif time == "AM" or time == "PM":
            new_times.append(time)
        else:
            new_times.append(int(time))

    if (new_times[0] < 0 or new_times[0] > 12) or (new_times[3] < 0 or new_times[3] > 12):
        raise ValueError
    if (new_times[1] < 0 or new_times[1] > 59) or (new_times[4] < 0 or new_times[4] > 59):
        raise ValueError

    if new_times[2] == "PM" and new_times[0] != 12:
        new_times[0] += 12
    if new_times[5] == "PM" and new_times[3] != 12:
        new_times[3] += 12
    if new_times[2] == "AM" and new_times[0] == 12:
        new_times[0] = 0
    if new_times[5] == "AM" and new_times[3] == 12:
        new_times[3] = 0

    return f"{new_times[0]:02d}:{new_times[1]:02d} to {new_times[3]:02d}:{new_times[4]:02d}"

if __name__ == "__main__":
    main()