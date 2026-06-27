import random

salary = []

for i in range(12):
    salary.append(random.randint(7500, 15000))

average = sum(salary) / len(salary)
print(f"Average: {round(average, 2)}$")
