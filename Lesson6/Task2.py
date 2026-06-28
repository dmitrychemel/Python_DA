list1 = {i for i in range(1,31) if i%3 == 0}
list2 = {i for i in range(1,31) if i%5 == 0}

set1 = set(list1) & set(list2)

print(set1)