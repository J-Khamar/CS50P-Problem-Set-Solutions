exp = input("Expression: ").split(" ")
x = int(exp[0])
y = int(exp[2])
operator = exp[1]

if operator == "+":
    print(float(x + y))
elif operator == "-":
    print(float(x - y))
elif operator == "*":
    print(float(x * y))
elif operator == "/":
    print(float(x / y))
