def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper

# Then:

@logger
def greet():
    print("Hello")

greet()

def get_numbers():
    for i in range(5):
        yield i

for i in get_numbers():
    print(i)
