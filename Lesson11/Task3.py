dates = ['2023-01-01', '2023-01-02', '2023-01-03']
temps = [5.5, 3.2, 4.0]

result = list(zip(dates, temps))

min_date, min_temp = min(result, key = lambda x: x[1])

print(f"Minimum temperature for {min_date} is {min_temp}")
