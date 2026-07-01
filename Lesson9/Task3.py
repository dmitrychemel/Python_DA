def count_keyword_occurrences(list, keyword):
    count = 0
    for item in list:
        if item.find(keyword) != -1:
            count += 1

    return count

print(count_keyword_occurrences(
    ["Hello world", "Python world", "DA for everyone"],
    "world"
))