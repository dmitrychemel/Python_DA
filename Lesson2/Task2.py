apartment_num = int(input("Enter number apartment"))

if apartment_num < 1 or apartment_num > 144:
    print("Error")

entrance = (apartment_num - 1) // 36
floor = (apartment_num - 1) % 36 // 4 + 1
print(f"entrance - {entrance} | floor - {floor}")
