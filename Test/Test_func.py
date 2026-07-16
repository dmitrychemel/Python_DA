from collections import defaultdict
from typing import Any
import statistics


def clean_quantity(orders):
    clean_orders = []

    for order in orders:
        if order["Quantity"] == "":
            order["Quantity"] = 0
        else:
            order["Quantity"] = int(float(order["Quantity"]))

        if order["Quantity"] < 0:
            continue

        clean_orders.append(order)

    return clean_orders


def clean_unit_price(orders):
    clean_orders = []

    for order in orders:
        if order["UnitPrice"] == "":
            continue

        order["UnitPrice"] = float(order["UnitPrice"])

        if order["UnitPrice"] <= 0:
            continue

        clean_orders.append(order)

    return clean_orders


def clean_discount(orders):
    clean_orders = []

    for order in orders:
        if order["Discount"] == "":
            order["Discount"] = 0.0
        else:
            order["Discount"] = float(order["Discount"])

        if order["Discount"] > 0.3:
            continue

        clean_orders.append(order)

    return clean_orders


def normalize_payment_method(orders):
    for order in orders:
        order["PaymentMethod"] = order["PaymentMethod"].upper()

    return orders


def clean_all(orders, *functions):
    for function in functions:
        orders = function(orders)

    return orders


def split_by_customer_id(orders):
    identified_orders = []
    unidentified_orders = []

    for order in orders:
        if order["CustomerID"] == "":
            unidentified_orders.append(order)
        else:
            identified_orders.append(order)

    return identified_orders, unidentified_orders


def group_by_category(orders: list) -> dict[str, list]:
    grouped_orders = defaultdict(list)
    for order in orders:
        grouped_orders[order["Category"]].append(order)

    return grouped_orders


def most_popular_item(orders: list) -> Any | None:
    if not orders:
        return ""

    popular_item = max(orders, key=lambda order: order["Quantity"])

    return popular_item["Description"]


def total_quantity(orders: list) -> Any | None:
    if not orders:
        return 0

    return sum(order["Quantity"] for order in orders)


def total_sales(orders: list) -> Any | None:
    if not orders:
        return 0

    return sum(order["Sales"] for order in orders)


def top_customer(orders: list) -> Any | None:
    if not orders:
        return ""

    max_orders_price = 0
    top_customer_id = ""

    for order in orders:
        price = order["Quantity"] * order["UnitPrice"] * (1 - order["Discount"])
        if price > max_orders_price:
            max_orders_price = price
            top_customer_id = order["CustomerID"]

    return top_customer_id


def top_category(orders: list) -> Any | None:
    group_orders = defaultdict(float)

    for order in orders:
        price = order["Quantity"] * order["UnitPrice"] * (1 - order["Discount"])
        category = order["Category"]
        group_orders[category] += price

    return max(group_orders, key=group_orders.get)


def sum_by_category(orders: list) -> Any | None:
    group_orders = defaultdict(list)

    for order in orders:
        price = order["Quantity"] * order["UnitPrice"] * (1 - order["Discount"])
        category = order["Category"]
        group_orders[category] += price

    return group_orders


def top_categories(orders: list, n: int = 3) -> Any | None:
    top_groups = sum_by_category(orders)

    sorted_groups = sorted(
        top_groups.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_groups[:n]


def payment_method(orders: list) -> Any | None:
    if not orders:
        return ""

    grouped_payments = defaultdict(list)
    for order in orders:
        grouped_payments[order["PaymentMethod"]].append(order)

    return grouped_payments


def average_discount(orders: list) -> Any | None:
    if not orders:
        return 0

    return sum(order["Discount"] for order in orders) / len(orders)


def best_category(orders: list) -> Any | None:
    category_sums = sum_by_category(orders)

    return max(category_sums, key=category_sums.get)


def total_sale_orders(orders: list) -> list:
    total_sales = []
    for order in orders:
        total_sales.append(order["Quantity"] * order["UnitPrice"] * (1 - order["Discount"]))

    return total_sales


def calculate_mean(orders: list) -> float:
    return statistics.mean(total_sale_orders(orders))


def calculate_median(orders: list) -> float:
    return statistics.median(total_sale_orders(orders))


def calculate_standard_deviation(orders: list) -> float:
    return statistics.stdev(total_sale_orders(orders))


def calculate_quartiles(orders: list) -> tuple:
    quartiles = statistics.quantiles(total_sale_orders(orders))

    q1 = quartiles[0]
    q3 = quartiles[2]
    iqr = q3 - q1

    return q1, q3, iqr


def is_normal_distribution(orders: list) -> bool:
    average = calculate_mean(orders)
    median = calculate_median(orders)

    difference = abs(average - median)
    good_difference = abs(median) * 0.1

    return difference < good_difference


def outliers(orders: list) -> list:
    outliers = []

    if is_normal_distribution(orders):
        average = calculate_mean(orders)
        deviation = calculate_standard_deviation(orders)

        lower_bound = average - 3 * deviation
        upper_bound = average + 3 * deviation

    else:
        q1, q3, iqr = calculate_quartiles(orders)

        lower_bound = q1 - 1, 5 * iqr
        upper_bound = q3 + 1.5 * iqr

    for order in orders:
        current_sum = order["Quantity"] * order["UnitPrice"] * (1 - order["Discount"])

        if current_sum > upper_bound or current_sum < lower_bound:
            outliers.append(order)

    return outliers


def compare_orders(orders: list) -> str:
    average = calculate_mean(orders)

    large_orders_sum = 0
    small_orders_sum = 0
    for order in orders:
        price = order["Quantity"] * order["UnitPrice"] * (1 - order["Discount"])

        if price > average:
            large_orders_sum += price
        else:
            small_orders_sum += price

    if large_orders_sum > small_orders_sum:
        return "Выгоднее штучные заказы на большую сумму"

    return "Выгоднее много заказов с небольшими суммами"


def compare_customer_orders(orders: list) -> str:
    identified_orders, unidentified_orders = split_by_customer_id(orders)

    identified_sum = sum(total_sale_orders(identified_orders))
    unidentified_sum = sum(total_sale_orders(unidentified_orders))

    if identified_sum > unidentified_sum:
        return "Большую общую сумму дают идентифицированные пользователи"

    elif unidentified_sum > identified_sum:
        return "Большую общую сумму дают неидентифицированные пользователи"

    return "Суммы заказов обеих групп одинаковые"


def compare_group_statistics(orders: list) -> str:
    identified_orders, unidentified_orders = split_by_customer_id(orders)

    identified_mean = calculate_mean(identified_orders)
    unidentified_mean = calculate_mean(unidentified_orders)

    identified_median = calculate_median(identified_orders)
    unidentified_median = calculate_median(unidentified_orders)

    identified_stdev = calculate_standard_deviation(identified_orders)
    unidentified_stdev = calculate_standard_deviation(unidentified_orders)

    print("Идентифицированные пользователи:")
    print("Среднее:", identified_mean)
    print("Медиана:", identified_median)
    print("Стандартное отклонение:", identified_stdev)

    print("\nНеидентифицированные пользователи:")
    print("Среднее:", unidentified_mean)
    print("Медиана:", unidentified_median)
    print("Стандартное отклонение:", unidentified_stdev)

    difference = abs(identified_mean - unidentified_mean)

    if difference <= identified_mean * 0.1:
        return "Существенной разницы между группами нет"

    if identified_mean > unidentified_mean:
        return "Средняя сумма выше у идентифицированных пользователей"

    return "Средняя сумма выше у неидентифицированных пользователей"


def discount_analysis(orders: list) -> str:
    discount_count = 0
    no_discount_count = 0

    for order in orders:
        if order["Discount"] > 0:
            discount_count += 1
        else:
            no_discount_count += 1

    print("Количество заказов со скидкой:", discount_count)
    print("Количество заказов без скидки:", no_discount_count)

    if discount_count > no_discount_count:
        return "Заказов со скидкой больше. Скидка привлекает покупателей."

    elif no_discount_count > discount_count:
        return "Заказов без скидки больше. Скидка не показывает положительного эффекта."

    return "Количество заказов со скидкой и без скидки одинаковое."
