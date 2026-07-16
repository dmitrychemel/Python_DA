import csv

from Test_func import *

file_address = "orders_project_01.csv"

with open(file_address, "r") as orders_project:
    reader = csv.DictReader(orders_project)
    orders = list(reader)

print("Количество записей:", len(orders))

orders = clean_all(
    orders,
    clean_quantity,
    clean_unit_price,
    clean_discount,
    normalize_payment_method
)

print("Количество очищенных записей:", len(orders))

print("Определите что выгоднее штучные заказы на большую сумму или много заказов с незначительными суммами.")
print(compare_orders(orders))

print()
print("Товары какой категории дают максимальные суммы?")
print(top_category(orders))

print()
print("Какой самый популярный товар?")
print(most_popular_item(orders))

print()
print("Какой самый популярный товар?")
print(most_popular_item(orders))

print()
print("Какие заказы дают большие суммы, там где пользователь идентифицирован или нет?")
print(compare_customer_orders(orders))

print()
print("Есть ли разница в статистиках для этих групп?")
print(compare_group_statistics(orders))

print()
print("Привлекает ли людей скидка на товар?")
print(discount_analysis(orders))

