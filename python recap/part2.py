users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

print(users[1]["name"])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]
print(squares)