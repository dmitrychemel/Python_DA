number = int(input("Enter number: "))

digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10

if (digit1 + digit2) == (digit3 + digit4):
    print("luck")
else:
    print("not luck")
