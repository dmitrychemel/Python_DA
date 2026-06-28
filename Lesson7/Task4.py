goods = ["IPhone 11", "Samsung Note 11", "Nokia 3310"]
prices = [500, 400, 1000]

products = {}

for element in goods:
    products[element] = prices[goods.index(element)]

print(products)
