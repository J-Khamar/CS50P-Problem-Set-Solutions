import csv
import sys
import tabulate

if len(sys.argv) < 2:
    exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    exit("Not a CSV file")

menu = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    exit("File does not exist")
else:
    pass

print(tabulate.tabulate(menu, headers="firstrow", tablefmt="grid"))