# Topics: Variables & types, Conditionals, Loops, Functions, Scope, Practical Python Habits, Interview-style thinking\

## 1. Variables & Python's Type System

### The Basic Idea

A variable is simply a name referring to an object in memory
Unlike languages such as C++/Java, Python doesn't require you to declare the type of a variable

```
name = "Omkar"
age = 21
salary = 75000.5
is_active = True
```

Python determines the type at runtime:
age = 21
print(type(age))

And a variable can later refer to a completely different type:
x = 10
x = "hello"
_this is called dynamic typing_

Important interview distinction
Python is:

- Dynamically typed -> type conversion happens at runtime
- Strongly typed -> python generally doesn't silently treat unrealted type as compatible
  for ex:
  "10" + 5
  o/p -> TypeError

### Common Built in types

#### Numbers

age = 21 #int
price = 99.99 #float

#### Boolean

is*logged_in = True
\_bool* is actually a subclass of _int_:
ex: print(True + True) #2

#### Strings

name = "Omkar"
print(name.upper())
print(name.lower())
print(len(name))

Strings are _immutable_
This means:
name = "hello"
name[0] = "H" #TypeError

instead:
name = "H" + name[1:] #this name[1:] means, take everything from index 1 to the end -> "ello"

#### _None_

_None_ represents **absence of a value**
_result = None_
A common interview question:
What's the difference between _None, False, 0, and ""_
They're different values, although all except _None_ can be falsy.
So, Prefer:

```
if result is None:
    ...
```

rather than:
if result == None:
...
_is_ checks **identity**; _==_ checks **equality**

## 2. Conditionals

Python uses indentation to define blocks.

```
age = 21

if age >= 18:
    print("Adult")
else:
    print("Minor")

#Multiple Conditions:
score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
```

#### Logical Operators

```
age = 25
has_id = True

if age >= 10 and has_id:
    print("Allowed")
```

You should know:

- _and_
- _or_
- _not_

#### Truthiness

Python lets you write:

```
items = []

if items:
    print("There are items")
```

An empty list is falsy

Common falsy values include:

- False
- None
- 0
- 0.0
- ""
- []
- {}
- set()
  This is extremely common in Python backend code.

## 3. Loops

There are two major loops

### _for_

Use _for_ when you're iterating over something

```
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Python's _for_ loop is essentially:
"Give me each item from this iterable"

We can loop through strings:

```
for char in "Python":
    print(char)
```

Dictionaries:

```
user = {
    "name" = "Omkar"
    "age" = 21
}

for key in user:
    print(key)
#or keys and values:
for key, value in user:
    print(key, value)
```

### _range()_

very common:

```
for i in range(5):
    print(i)
```

o/p:
0
1
2
3
4

Important:
_range(start, stop, step)_
Example:

```
for i in range(0, 10, 2):
    print(i)
0
2
4
6
8
```

The _stop_ value is **excluded**

### _while_

Use _while_ when the loop depends on a condition

```
count = 0

while count < 3:
    print(count)
    count += 1
```

Be careful about **infinite loops**:

```
count = 0

while count < 3:
    print(count)
```

_count_ never changes, so the loop never terminates.

### _break_ and _continue_

_break_ exits the loop:

```
for number in range(10):
    if number == 5:
        break
    print(number)
```

_continue_ skips the current iteration:

```
for number in range(5):
    if number == 2:
        continue
    print(number)
```

## 4. Functions

Functions are one of the most important Python concepts for backend development
A function lets you package reusable behavior

```
def add(a, b)
    return a + b
```

Calling it:

```
result = add(10, 20)
print(result)
```

### Parameters vs arguments

```
def greet(name):
    print(f"Hello {name}")
```

_name_ is a **parameter**
_greet("Omkar")_
_"Omkar"_ is an **argument**

Parameter = a variable listed inside the parentheses of a function definition
Argument = the actual value or object passed into a function or method when you call it

### Return Values

A function without an explicit _return_ returns _None_

```
def greet(name):
    print(f"Hello {name}")

result = greet("Omkar")

print(result)
```

_result_ is:
_None_

Compare:

```
def add(a, b):
    return a + b
```

Here the caller gets the result.

### Default arguments

```
def greet(name, greetings="Hello"):
    return f"{greeting}, {name}"

print(greet("Omkar"))
print(greet("Omkar", "Hi"))
```

### Keyword arguements

```
def create_user(name, age):
    print(name, age)

create_user(age = 21, name="Omkar")
```

This improves readability and avoids relying on argument position.

### Type hints

You will see these constantly in FastAPI'

```
def add(a: int, b: int) -> int:
    return a + b
```

Important interview point:
**Type hints don't normally enforce types at runtime by themselves**
They're primarily metadata for:

- developers
- IDEs
- static type checkers
- frameworks such as FastAPI
  FastAPI uses type annotations heavily for request validation and dependency handling

## 5. Scope

This is particularly important for interviews
Consider:

```
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

o/p:
20
10

Why?
Because the _x_ inside the function is a **local variable**
The _x_ outside is a **global variable**

### **LEGB Rule**

When Python looks for a variable, it searches roughly in this order:
L -> Logical
E -> Enclosing
G -> Global
B -> Built-in

Ex:

```
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
```

_inner()_ finds the local _x_ first.

### _global_

You can explicitly modify a global variable

```
count = 0
def increment():
    global count
    count += 1
```

But in backend code, excessive use of globals is generally a bad design
Prefer passing values into functions or using appropriate objects/dependencies.

## 6. A critical Python interview concept: mutable vs immutable

Common immutable objects:
int
float
bool
str
tuple

Common mutable objects:
list
dict
set

Ex:
_name = "Omkar"_
You cannot modify the string itself

But:
_numbers = [1, 2, 3]_
_numbers.append(4)_
modifies the existing list

This distinction becomes very important when passing objects into functions.

## 7. One backend/fintech-specific point: _float_ vs _Decimal_

Don't blindly use:
_price = 0.1 + 0.2_
_print(price)_
You may get:
0.3000000000000004

Why?
Binary floating-point numbers cannot represent many decimal fractions exactly.

For financial values, _Decimal_ is often more appropriate:

```
from decimal import Decimal

price = Decimal("0.1") + Decimal("0.2")
print(price)
```

Result:
0.3

Also notice:
_Decimal("0.1")_
is preferable to:
_Decimal(0.1)_
because the latter starts from the already-inexact binary float

Interview answer,
if asked:
"Would you use float for storing monetary values?"
A good answer is:
Generally no. For monetary calculations where exact decimal arithmetic matters, I'd prefer Decimal or a database representation such as integer monitor units, depending on the system's design. Float is appropriate for many scientific or approximate calculations but can introduce binary floating-point precision issues.

## 8. Part 1 - Mini challenge

q1. What's the difference between dynamic typing and strong typing in Python?
a variable can change its value as the code gets progressively bigger, and strong typing means if a variable or a function is wront in python, python points it out -> it points out the error

q2. predict output and why

```
x = 10

def test():
    x = 20
    return x

print(test())
print(x)
```

20
10
cause first the function test is called and it has a local variable and then the global variable is called

q3. Write a function:
_is_even(number)_
that returns true or false if even

```
def is_even(numbers):
    return number % 2 == 0
    <!-- if numbers%2 == 0:
        return "True"
    else:
        return "False" -->

print(is_even(4))
```

q4. Backend/fintech
You're implementing a portfolio system that calculates:
_$10,000.10 + $20,000.20_
Would you use _float_ or _Decimal_? Why?
-> I will use Decimal cause of the float decimal precision problem
