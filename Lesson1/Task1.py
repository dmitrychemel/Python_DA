import math

sideA = 0.3
sideB = 0.4
sideC = 0.5

p = (sideA + sideB + sideC) / 2

area = math.sqrt(p * (p - sideA) * (p - sideB) * (p - sideC))

print(area)