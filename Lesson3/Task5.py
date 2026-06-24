import math

number = int(input("Inter number: "))
stars = 1
temp = 0

for i in range(number * 2 - 1):
    if stars == number:
        print("*" * (stars - temp))
        temp = temp + 1
    else:
        print("*" * stars)
        stars = stars + 1
