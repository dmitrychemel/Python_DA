apple = input("Enter number of apples: ")
price = 2

if apple.isdigit():
    apple = int(apple)
    print(f"The cost of {apple} apples is ${price * apple}")
else:
    print("It is not a number.")