# # # name = "hello"
# # # name = "H" + name[1:]   # TypeError

# # # print(name)

# # items = []

# # if items:
# #     print("There are items")

# numbers = [10, 20, 30]

# for number in numbers:
#     print(number)

# # for char in "Python":
# #     print(char)

# count = 0

# while count < 3:
#     print(count)
#     count += 1

# # for number in range(10):
# #     if number == 5:
# #         break
# #     print(number)

# for number in range(5):
#     if number == 2:
#         continue
#     print(number)

# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}"

# print(greet("Omkar"))
# print(greet("Omkar", "Hi"))

def is_even(numbers):
    if numbers%2 == 0:
        return "True"
    else:
        return "False"

print(is_even(4))