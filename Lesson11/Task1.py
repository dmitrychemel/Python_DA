def filter_clients(clients, **criteria):
    result = []

    for client in clients:
        if "min_age" in criteria:
            if client["age"] < criteria["min_age"]:
                continue

        if "max_age" in criteria:
            if client["age"] > criteria["max_age"]:
                continue

        if "country" in criteria:
            if client["country"] != criteria["country"]:
                continue

        result.append(client)

    return result

clients = [
    {'name': 'Alice', 'age': 28, 'country': 'USA'},
    {'name': 'Bob', 'age': 35, 'country': 'Canada'},
    {'name': 'Carol', 'age': 40, 'country': 'USA'},
]

print(filter_clients(clients, min_age=20, max_age=50, country='USA'))