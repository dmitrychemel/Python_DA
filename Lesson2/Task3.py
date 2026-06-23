year = int(input("Enter YEAR "))

if year % 400 == 0:
    print("366")
elif year % 100 == 0:
    print("365")
elif year % 4 == 0:
    print("366")
