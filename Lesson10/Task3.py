def max_quarter(list_num):
    if len(list_num) != 12:
        print("Error")

    q1 = list_num[0:3]
    q2 = list_num[3:6]
    q3 = list_num[6:9]
    q4 = list_num[9:]

    quarters = {
        "Q1": q1,
        "Q2": q2,
        "Q3": q3,
        "Q4": q4
    }

    return max(quarters, key=quarters.get)


print(max_quarter([1200, 1300, 1500, 2000, 2100, 2500, 3000, 3100, 2800, 2200, 2300, 2100]))
