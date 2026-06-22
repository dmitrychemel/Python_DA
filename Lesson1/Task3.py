fuel_price = 1.2
fuel_consumption = 8
distance = 120

fuel_needed = distance / 100 * fuel_consumption

cost = fuel_needed * fuel_price
print(f"{cost}$")