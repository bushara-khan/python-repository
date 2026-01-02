num1 = float(input("Pehla number daalein: "))
op = input("Operation chunein (+, -, *, /): ")
num2 = float(input("Doosra number daalein: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Zero se divide nahi kar sakte.")
else:
    print("Invalid operation.")