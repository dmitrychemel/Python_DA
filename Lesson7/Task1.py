week = {1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"}

number = int(input("Insert an integer: "))
if number > 7:
    print("error")
else:
    print(week[number])
