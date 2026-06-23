number = int(input("Enter number: "))

digit1 = number // 100000
digit2 = (number % 100000) // 10000
digit3 = (number % 10000) // 1000
digit4 = (number % 1000) // 100
digit5 = (number % 100) // 10
digit6 = number % 10

if digit1 == digit6 and digit2 == digit5 and digit3 == digit4:
    print("Is palindrome")
else:
    print("Is not palindrome")
