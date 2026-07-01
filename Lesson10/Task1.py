from collections import defaultdict

list_1 = [ ("Alice", "Book"), ("Alice", "Pen"), ("Bob", "Book") ]

def group(list_input):
    result = defaultdict(list)

    for name, product in list_input:
        result[name].append(product)

    return result

print(group(list_1))