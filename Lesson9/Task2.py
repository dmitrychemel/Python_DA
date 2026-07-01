def above_threshold(list, threshold):
    count = 0
    for item in list:
        if threshold >= item:
            count += 1

    return count

print(above_threshold([10, 15, 20, 8], 12))