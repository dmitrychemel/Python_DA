number = int(input("Inter number: "))

if 4 < number < 16:
    faktorial = number
    for i in range(number - 1, 1, -1):
        faktorial = faktorial * i
    print(faktorial)
else:
    print("error")
