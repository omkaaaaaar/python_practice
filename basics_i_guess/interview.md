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

### 3. Question:

```
text = "Python AI"

print(text[0:6])  #Python
print(text[::-1])  # IA nohtyP
print(text.split())  # ['Python', 'AI']
print("-".join(text()))  # TypeError: 'str' objext is not callable
print("-".join(text.split()))  # Python-AI
```

## Topic 4: List Operations

### Explanation

Lists are **ordered and mutable**. Common interview operations include adding (_append_), removing (_pop, remove_), sorting (_sort, sorted_), slicing, and list compreshensions. Remember that _sort()_ modifies the original list, while _sorted()_ returns a new sorted list. List object has no attribute/operation _'sorted'_ btw, we'll need to always use it with print(sorted(_lst_)) we cant use lst.sorted()

### 2. Code Example

```
nums = [3, 1, 2]

nums.append(4)
print(nums)    # [3, 1, 2, 4]

nums.pop()    # last element/recent added elements gets popped
print(nums)    # [3, 1, 2]

nums.remove(1)
print(nums)    # [3, 2]

print(sorted(nums))    # [2, 3]

nums.sort()
print(nums)    # [2, 3]

print(nums[::-1])    # [3, 2]

squares = [x*x for x in range(5)]    # this equation means, x = x times x for the range of 5 (0,1,2,3,4)
print(squares)    # [0, 1, 4, 9, 16]

```

### 3. Question:

```
nums = [5, 2, 4, 2]

nums.remove(2)
print(nums)    # [5, 4, 2], the 1st 2 from the left/ SI gets removed/ first occurence of 2 gets removed
nums.append(10)
print(nums)    # [5, 4, 2, 10]

print(nums)    # [5, 4, 2, 10]
print(sorted(nums))    # [2, 4, 5, 10]
print(nums[1:4])    # [4, 2, 10]
```

## Topic 5: Tuple and Set

### 1. Explanation

- **Tuple:** Ordered and **immutable**. Use it for fixed data that shouldn't change(e.g., employee = ("Omkar", 21, "Developer"))
- **Set:** Unordered, **mutable**, and stores **unique** elements only.
- Sets automatically remove duplicates and are very fast for membership checks (_in_).

### 2. Code Example:

```
# Tuple
point = (10, 20)
print(point[0])    # 10

# Set
nums = {1, 2, 2, 3, 3, 4}
print(nums)    # {1, 2, 3, 4} (order not guaranteed)

nums.add(5)
print(nums)    # {2, 3, 1, 4, 5}
nums.remove(2)
print(nums)    # {1, 3, 5, 4}
print(3 in nums)    # True
```

### 3. Question:

```
t = (1, 2, 3)

s = {1, 2, 2, 3}
s.add(4)

print(len(t))    # 3
print(3)    # {2, 1, 4, 3}
print(2 in s)    # True
```

## Topic 6: Dictionary

### 1. Explanation

A dictionary stores **key-value pairs.** Keys must be **unique and hashable** (e.g., _str, int, tuple_), while values can be any type. Dictionaries are mutable and provide **O(1)** lookup by key.
Common interview methods:

- _dict[key]_
- _.get()_
- _.items()_
- _.keys()_
- _.values()_
- _.update()_
- _del_

### 2, Code Example;

```
student = {
    "name": "Omkar",
    "age": 21,
    "marks": {
        "python": 95,
        "ai": 92
    }
}

print(student["name"])    # Omkar
print(student.get("city"))    # None

student["age"] = 22
student["city"] = "Mumbai"
print(student.get("city"))    # Mumbai

print(student.keys())    # dict_keys(['name', 'age', 'marks', 'city'])
print(student.values())    #dict_values(['Omkar', 22, {'python': 95, 'ai': 92}, 'Mumbai'])
print(student.items)    #dict_items([('name', 'Omkar'), ('age', 22), ('marks', {'python': 95, 'ai': 92}), ('city', 'Mumbai')])

print(student["marks"]["python"])    # 95

del student["city"]
print(student)
```

### 3. Check Question

```
person = {
    "name": "Alice",
    "age": 25
}

print(person.get("city"))    # None
person["age"] = 26
person["country"] = "India"

print(person["age"])    # 26
print(person.keys())    # dict_keys(['name', 'age', 'country'])
print(person.values())    # dict_values(['Alice', 26, 'India'])
```

**Interview Tips**
_dict[key]_ vs _.get()_

d = {"a": 1}
print(d["a"]) # 1
print(d.get("a")) # 1

Missing key:
print(d["b"]) # keyError ❌
print(d.get("b")) # None

So use _.get()_ when a key may not exist.
