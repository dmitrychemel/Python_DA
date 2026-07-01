def valid_users(users):
    result = []

    for user in users:
        if all(user.values()):
            result.append(user)

    return result

print(valid_users([
        {"login": "Alice", "country": "USA", "email": "alice@mail.com"},
        {"login": "Bob", "country": "", "email": "bobby@mail.com"},
        {"login": "Charlie", "country": "USA", "email": ""}
    ]))
