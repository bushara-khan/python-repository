name = input("Enter your name: ")
n = int(input("Enter a number: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print(i, name, "Even")
    else:
        print(i, name, "Odd")
