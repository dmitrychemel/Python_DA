import random

list1 = []

for i in range(4):
  list1.append(random.randint(1,10))

list2 = list1.copy()

for i in range(len(list1)):
  list2.append(list1[i] * 2)

