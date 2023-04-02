month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "/" in date:
        date = date.split("/")
    elif "," in date:
        date = date.split(" ")
        date[1] = date[1].rstrip(",")
        if date[1].isalpha() or date[2].isalpha():
            continue
        date[0] = month.index(date[0]) + 1
    else:
        continue

    try:
        date[0] = int(date[0])
        date[1] = int(date[1])
        date[2] = int(date[2])
    except ValueError:
        continue
    else:
        if (date[0] < 0 or date[0] > 12) or (date[1] < 1 or date[1] > 31) or (date[2] < 1):
            continue
        else:
            break

print(f"{date[2]:04d}-{date[0]:02d}-{date[1]:02d}")
