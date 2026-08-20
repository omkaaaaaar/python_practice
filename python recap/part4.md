# Part 4: Decorators, Iterators, Generators, Context Managers, Exception handling, Custom Exceptions

## 4.1 Decorators - What problem do they solve?

Imagine you have:

```
def greet():
    print("Hello")
```

Now you want to add logging:
When greet() runs:

1. Print "Function Started"
2. Run greet()
3. Print "Function Finished"

You could modify _greet()_ directly
But what if you have 50 functions?
Instead, Python gives us **decorators**

A decorator lets you **wrap a function and add behavior without modifying its core code**

**The basic idea**

```
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
```

This:
_@logger_
_def greet():_
is essentially equivalent to:
_greet = logger(greet)_

## 4.2 Why decorators matter for FastAPI

You'll encounter patterns such as:

```
@app.get("/users")
def get_users():
    ...
```

The _@app.get(...)\_ syntax is a decorator

It essentially tells FastAPI:
"Register this function as the handler for this HTTP route"

**FastAPI uses decorators heavily**

## 4.3 Decorators with arguments

Real function often accept arguments

```
def logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("function finished")

    return wrapper

# then

@logger
def add(a, b):
    return a + b
```

Now:
_result = add(10, 20)_
works correctly

*args:
The *args allows to insert any number of positional arguments into the function

**kwargs
the **kwargs allows to insert any number of keyword arguments into the function

**Why** \*_args_, \*\*kwargs?
Because the decorator shouldn't need to know exactly how many arguments the wrapped function takes
It can accept arbitrary positional and keyward arguments and forward them:
func(\*args, \*\*kwargs)

## 4.4 Generators

A generator produces values **lazily**, one at a time, rather than creating the entire collection in memory at once

Normal function:

```
def get_numbers():
    return [1, 2, 3, 4, 5]
```

The whole list exists in memory

Generator:

```
def get_numbers():
    for i in range(5):
        yield i
```

Notice:
_yield_
Instead of:
_return_

You can iterate:
for number in get_numbers:
print(number)

### Why generators?

Imagine processing 10 million transactions
Doing
_transactions = load_all_transactions()_
could require a huge amount of memory

A generator can produce transactions one at a time:

```
def transactions():
    for transaction in transactions:
        yield transaction
```

This is called **lazy evaluation**

"A generator produces values lazily using _yield_, allowing us to process data one item at a time without loading the entire dataset into memory"
Very useful for:

- large datasets
- file processing
- streaming
- pipelines

## 4.5 Iterators

A generator is a type of iterator
An iterator is an object that provides values one at a time through the iterator protocol

THe key concepts are:
_iter()_
_next()_

Example:

```
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
```

Then:
_next(iterator)_
raises:
**StopIteration**
because there are no more values

**Iterable -> something you can iterate over**
**Iterator -> Object that produces next value**
**Generator -> convenient way to create an iterator**

## 4.6 Context Managers

You've probably seen:

```
with open("file.txt") as file:
    data = file.read()
```

Why _with_?
Because Python can automatically handle setup and cleanup
Conceptually:
enter resource
↓
use resource
↓
cleanup resource

For a file:
open file
↓
read/write
↓
close file

Even if an exception occurs, the context manager can ensure cleanup
This is extremely important in backend systems for things like:

- database connections
- files
- locks
- network resources

## 4.7 Exception Handling

Basic structure:

```
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

The potentially dangerous operation goes inside _try_
If the expected exception occurs, _except_ handles it

### Multiple exceptions

```
try:
    value = int(user_input)
except ValueError:
    print("Invalid number")

# we canhave multiple handlers:
try:
    ...
except ValueError:
    ...
except TypeError:
    ...

# prefer catching specific exceptions rather than:
except Exception:
    ...
# everywhere
```

## 4.8 else

_else_ runs if **no exception occured**

```
try:
    number = int("100")
except ValueError:
    print("Invalid")
else:
    print("Suncessfully converted")
```

Think:
try
↓
exception? → except
↓
no exception → else

## 4.9 finally

_finally_ runs whether or not an exception occurs

```
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File missing")
finally:
    print("Cleanup")
```

This is useful for cleanup operations
Although in modern Python, a context manager is often preferable for resources such as files

## 4.10 raise

You can deliberately raise anexception:

```
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient Balance")

    return balance - amount
```

then:
_withdraw(1000, 1500)_
raises:
ValueError: Insufficient balance

This becomes very relevant in API development
Later, FastAPI can translate appropriate errors into HTTP responses

## 4.11 Custom Exceptions

You can create your own exception type:

```
class InsufficientFundsError(Exception):
    pass

# then:

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds")

    return balance - amount
```

Why bother?
Because your application can distinuish:
_InsufficientFundsError_
from:
_DatabaseError_
or:
_AuthenticationError_
rather than treating every problem as a generic _Exception_
