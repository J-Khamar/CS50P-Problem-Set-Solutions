list = {}

while True:
    try:
        item = input("").upper().strip()
    except EOFError:
        print()
        break

    if item in list:
        list[item] += 1
    else:
        list[item] = 1

list = sorted(list.items())

for item in list:
    print(f"{item[1]} {item[0]}")