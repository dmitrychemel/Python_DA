first_side = int(input("Enter first side: "))
second_side = int(input("Enter second side: "))
third_side = int(input("Enter third side: "))

if (first_side + second_side) <= third_side:
    print("error")
elif (third_side + second_side) <= first_side:
    print("error")
elif (first_side + third_side) <= second_side:
    print("error")
else:
    print("good")
