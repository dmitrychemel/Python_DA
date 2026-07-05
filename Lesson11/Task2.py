from functools import reduce

new_users = [10, 15, 7, 20]

current = 0
day = 0

for user in new_users:
    if current > 30:
        break
    else:
        current += user
        day += 1



print(f"All new users: {reduce(lambda x, y: x + y, new_users)}, more than 30 users in day: {day}")


