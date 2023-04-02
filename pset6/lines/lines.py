from sys import argv, exit

if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")

if not argv[1].endswith(".py"):
    exit("Not a Python file")

try:
    file = open(argv[1])
except FileNotFoundError:
    exit("File does not exist")
else:
    pass

counter = 0

for line in file:
    if line.isspace() == False and not line.lstrip().startswith("#") == True:
        counter += 1

print(counter)

