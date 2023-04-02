import csv
import sys

student = []

try:
    with open("before.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            student.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
else:
    pass

with open("after.csv", 'w', newline='') as file:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in student:
        writer.writerow(row)
