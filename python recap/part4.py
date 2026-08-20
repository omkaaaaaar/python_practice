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

class InsufficientFundsError(Exception):
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError("Not enough balance")

    return balance

