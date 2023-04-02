due = 50

while due > 0:
    print(f"Amount due: {due}")
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due -= coin

if due <= 0:
    print(f"Change owed: {0 - due}")