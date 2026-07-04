# Python Interview Prepartion

## Phase 1

## Topic 1: Data Types

1. Theory
   Python has built-in data types to store different kinds of values:

- int -> whole numbers (10, -5)
- float -> decimal numbers (3.14)
- str -> text ("Hello")
- bool -> _True_ or _False_
- list -> ordered, mutable collection (_[1,2,3.14,True,"Omkar"]_), can store mixed data type, they preserve the insertion order, (if 2,3,1 added in a list it won't be 1,2,3 it will be stored as 2,3,1 only) and not the sorted order
- tuple -> ordered, immutable collection (_[1,2,3,"hello",3.14,True]_), can store mixed data types, it only keeped the insertion order and not the automatically sorted order
- set -> unordered, unique values (_{1,2,3}_), can store mixed data types (as long as the elements are hashable, so we can't put a list inside a set), sets they are unordered -> s={1,2,3} print(s) o/p could be: {2,3,1}, also not automatically sorted the are random
- dict -> key-value pairs (_{"name":"Omkar"}_), can add mixed data types, it keeps insertion order, not automatically sorted and are mutable, cannot have duplicate keys

2. Code

```
a = 10 #int
b = 3.5 #float
c = "23" #string
d = True #bool

nums = [1,2,3] #list
point = (10, 20) #tuple
colors = {"red", "blue"} #set
user = {"name":"Omkar", "age": 21} #dict

x = int(c) #"25" -> 25
y = str(a) #10 -> "10"
z = float(a) #10 -> 10.0
```

3. Question

```
x = "15"
y = 5

print(int(x) + y)
print(type(float(x)))
```

o/p:
20
float

## Topic 2: Mutable vs Immutable

### 1. Explaination

- **Mutable** objects can be changed after creation
- **Immutable** objects cannot be changed; any modification creates a new object
- Mutable: _list, dict, set_
- Immutable: _tuple, int, float, str, bool_
- This matters because mutable objects passed a functions can be modified in place.

### 2. Code Ex:

```
# Mutable
lst = [1,2]
lst.append(3)
print(lst)  #[1,2,3]

# Immutable
s = "hello"
s = s.upper()
print(s) # HELLO
```

### Question

```
a = [1,2]
b = a
b.append(3)

print(a)
print(b)
```

o/p:
_[1, 2, 3]_
_[1, 2, 3]_

Why?
When we do:
a = [1, 2]
b = a
we are not creating a new list. We're making _b_ point to the **same list object** as _a_.

```
Think of it like this:
a ─────┐
       ▼
    [1, 2]

b ─────┘

Now when we do:
b.append(3)
we're modifying that SINGLE SHARED LIST.
a ─────┐
       ▼
 [1, 2, 3]

b ─────┘
so:
print(a)   # [1, 2, 3]
print(b)   # [1, 2, 3]
```

Both variables show the same updated list because they reference to the same object.

**If want an actual copy insted:**

```
a = [1,2,3]
b = a.copy()   # or b = a[:]

b.append(3)

print(a) #[1,2]
print(b) #[1,2,3]
```

Here, _a_ and _b_ refer to **different list objects**, so changing one doesn't affect the other.

```
x = "hello"
y = x

y = y.upper()

print(x)   # hello
print(y)   # HELLO
```

Why?
Initially, both _x_ and _y_ point to the same string object:
Then:
_y = y.upper()_
Strings are **Immutable**. _upper()_ **does not modify** the original string. Instead, it creates a **new string** _"HELLO"_ and makes _y_ point to it.
Now the references look like this:
x ───► "hello"
y ───► "HELLO"
So:
print(x) # hello
print(y) # HELLO

**Interview Rule to Remember**

- **Mutable** (_list, dict, set_) -> changes happen **in place**.
- **Immutable** (_int, float, str, tuple, bool_) -> "changes" creates a **new object**.

## Topic 3: String Manipulation

### 1. Explantaion

Python strings are **immutable,** so string methods return a **new string** instead of modifying the original. Common interview methods include slicing, reversing, splitting, joining, stripping whitespace, finding substrings, replacing text, couting occurences, and changing case.

### 2. Code:

```
s = "  Hello World  "

print(s[0:5])  # '  Hel' (slicing, [starting index:ending index])
print(s[::-1])  # reverse a string, o/p -> dlorW olleH

print(s.strip())  # remove white space, o/p -> 'Hello World'
print(s.split())  # ['Hello', 'World']

print("-".join(["AI", "ML"]))  # AI-ML

print(s.find("World"))  # idex of World, o/p -> 8
print(s.replace("World", "Python"))  # Hello Python

print(s.count("l"))  # 3

print(s.upper())  # HELLO WORLD
print(s.lower())  #hello world
```
