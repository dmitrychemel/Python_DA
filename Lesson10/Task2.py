import statistics


def find_outliers(arr):
    if len(arr) < 2:
        return []

    avg = statistics.mean(arr)
    stdev_numbers = statistics.stdev(arr)

    outliers = []

    for num in arr:
        if abs(num-avg) > stdev_numbers:
            outliers.append(num)

    return outliers

list_numbers = [3600, 2578, 3152, 6300, 2195, 14800, 3378, 2003, 2948, 2080, 2040, 3232]

print(find_outliers(list_numbers))