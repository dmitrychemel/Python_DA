employees = [
    {"name": "Olga", "depatment": "hr"},
    {"name": "Inna", "depatment": "test"},
    {"name": "Alex", "depatment": "developer"},
    {"name": "Anna", "depatment": "developer"},
    {"name": "Ira", "depatment": "hr"}
]

group = {}

for employee in employees:
    depatment = employee["depatment"]
    name = employee["name"]

    if depatment in group:
        group[depatment].append(name)
    else:
        group[depatment] = [name]

print(group)