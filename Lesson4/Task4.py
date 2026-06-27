matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for row in matrix:
    print(row)

total = 0
for row in matrix:
    for e in row:
        total += e

print(total)
