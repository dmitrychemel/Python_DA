first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
fourth_number = int(input("Enter fourth number: "))

max_number = first_number

if second_number > max_number:
    max_number = second_number

if third_number > max_number:
    max_number = third_number

if fourth_number > max_number:
    max_number = fourth_number

print(max_number)
