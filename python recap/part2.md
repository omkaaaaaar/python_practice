# Part 2; Topics: _list_, _tuple_, _set_, _dict_, mutability, indexing, common operations & Big-O, comprehensions, choosing the right data structure, backend use cases

## 2.1 List

A list is ordered, mutable collection
_numbers = [10, 20, 30]_
we can modify it:

```
numbers.append(40)

print(numbers)
# [10, 20, 30, 40]
```

You can access by index:
_print(numbers[0])_ # 10
_print(numbers[-1])_ # 30

Because lists maintain order, they're useful when **position/ order matters**

Backend examples:

```
users = ["Alice", "Bob", "Charlie"]
or
transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 200},
]
```

## 2.2 Tuple

A tuple is an **ordered, immutable collection**
_point = (10, 20)_
We can read:
_print(point[0])_
But we can't modify:
_point[0] = 50_
That raises _TypeError_

So the basic comparison is:

```
|             | List                | Tuple            |
| ----------- | ------------------- | ---------------- |
| Ordered     | Yes                 | Yes              |
| Mutable     | Yes                 | No               |
| Indexing    | Yes                 | Yes              |
| Typical use | Changing collection | Fixed collection |
```

## 2.3 Set

A set stores **unique values**.

```
numbers = {1, 2, 3, 3, 3}
print(numbers)
```

Result:
{1, 2, 3}
Duplicates disappear

The most important reason to use a set is often **fast membership testing:**

```
allowed_roles  = {"admin", "manager", "analyst"}

if role in allowed_roles
    ...
```

Conceptually, you should think of a set as:
_I care whether this value exists, not where it is._

Unlike lists, sets don't provide normal postional indexing
_numbers[0]_
is invalid

## 2.4 Dictionary

A dictionary stores **key -> value mappings**

```
user = {
    "name": "Omkar",
    "age": 21
}
```

Access:
_print(user["name"])_

We can modify:
_user["age"] = 22_

And add:
_user["role"] = "backend_developer"_

Dictionaries are extremely important in backend Python because JSON objects naturally map to Python dictionaries

For example, an API response might conceptually look like:

```
{
    "user_id": 123,
    "name": "Omkar"
    "balance": 50000
}

which maps naturally to:
{
    "user_id": 123,
    "name": "Omkar",
    "balance": 50000
}
```

### Interview Question

q. What's the difference between a list, tuple, set and dictionary?
List: ordered collection where duplicates are allowed and modification is needed.
Tuple: ordered collection that should remain immutable
Set: unique values where fast membership testing is important
Dictionary: key-value mapping where I need to retrieve values by key

q1. You need to store 1,000 user IDs and repeatedly ask:
"Does this user ID exist?"
Would you choose a _list_ or _set_? Why?
I would use a set because the primary operation is repeatedly checking whether a user ID exists. Set membership checks are O(1) on average, while searching a list is O(n).

q2. What's the main difference between a _list_ and a _tuple_
List and tuple although function the same -> Ordered, Indexing but the main difference in it is that tuple are immutable while list is mutable

q3. Given:

```
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]
```

print(users[1]["name"])

## 2.5 Time Complexity - Very important

In interview, you will often hear:
"What's the time complexity of this operation?"
You don't need advance mathematics. Think of it as:
**How does the amount of work grow as the amount of data grows?**

This are the most common complexities you'll encounter

```
| Complexity     | Meaning                  | Example              |
| -------------- | ------------------------ | -------------------- |
| **O(1)**       | Constant                 | Dictionary lookup    |
| **O(log n)**   | Grows slowly             | Binary search        |
| **O(n)**       | Linear                   | Searching a list     |
| **O(n log n)** | Common efficient sorting | `sorted()`           |
| **O(n²)**      | Nested iteration         | Comparing every pair |
```

## 2.6 List Complexity

Consider:
_numbers = [10, 20, 30, 40, 50]_

### Access by index

_numbers[2]_
**O(1)**
Python can directly locate the element based on its index

### Append

_numbers.append(60)_
Usually **O(1) amortized**
One should say:
"List append is amortized O(1)"
Why "Amortized"?
Python occasionally needs to allocate a larger underlying array and move elements, but across many appends the average cost is constant

### Insert at begining

_numbers.insert(0, 5)_
O(n)
Why?
Existing elements need to be shifted.

```
Before:
[10, 20, 30, 40]

Insert 5:

[5, 10, 20, 30, 40]
     ↑  ↑  ↑   ↑
     elements shifted
```

### Remove from begining

_numbers.pop(0)_
O(n)
Again, elements have to shift
But:
_numbers.pop()_
is O(1) amortized

### Searching

```
if 30 in numbers:
    ...
```

for a list, membership testing is O(n) in the worst case
Python may have to examine every element

## 2.7 Dictionary Complexity

Consider

```
users = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}
```

Lookup:
_users[102]_
Average:
O(1)
Likewise:
_102 in users_
Average:
O(1)
And:
_users[104] = "David"_
Average:
O(1)
This is because dictionaries use a **hash table** internally

## 2.8 Why Does a Dictionary Give Fast Lookup?

Suppose we have:

```
users = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}
```

Python hashes the key
Conceptually:
101 -> hash function -> location
102 -> hash function -> location
103 -> hash function -> location

Instead of scanning:
Alice
Bob
Charlie
...
Python can use the hash to find the appropriate location

That's why dictionary lookup is **average O(1)**

q. Is dictionary lookup always O(1)?
Average case lookup is O(1) because dictionaries are hash tables. There can be collisions and worst-case behavior can differ, but O(1) average lookup is the practical complexity we normally quote

## 2.9 Set Complexity

Sets also use hashing
Therefore:
_numbers = {10, 20, 30, 40}_
_20 in numbers_
is O(1) average

Compare:
_numbers = [10, 20, 30, 40]_
_20 in numbers_
Which is **O(n)**

**This is an extremely useful pattern**
Suppose:
_blocked_users = [101, 205, 309, 450, ...]_
and you're repeatedly checking:
_if user_id in blocked_users:_
If there are many IDs, converting to:
_blocked_users = {101, 205, 309, 450}_
can make membership checks much

## 2.10 Tuple Complexity

Tuples are similar to lists for many operators
_point = (10, 20, 30)_
_point[1]_
is O(1)

But tuples are immutable
Why might this be useful?
If we have a fixed value:
_coordinates = (19.0760, 72.8777)_
we don't want random code accidentally changing the coordinates

## 2.11 The Data Structure Cheat Seat

```
| Operation         |           List | Tuple |      Set |            Dict |
| ----------------- | -------------: | ----: | -------: | --------------: |
| Index access      |           O(1) |  O(1) |        ❌ |               ❌ |
| Search/membership |           O(n) |  O(n) | O(1) avg |        O(1) avg |
| Append            | O(1) amortized |     ❌ | O(1) avg | O(1) avg insert |
| Insert beginning  |           O(n) |     ❌ |      N/A |             N/A |
| Delete            | O(n) generally |     ❌ | O(1) avg |        O(1) avg |
| Mutable           |              ✅ |     ❌ |        ✅ |               ✅ |
| Duplicates        |              ✅ |     ✅ |        ❌ |          Keys ❌ |
```

The **big three** to know are:
List indexing -> O(1)
List membership -> O(n)
Dict/set membership -> O(1) average

## 2.12 List Comprehensions

Reducing the lines of codes for list

Instead of:

```
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)
```

We can write:
squares = [number ** 2 for number in numbers]

With a condition:

```
numbers = [1, 2, 3, 4, 5, 6]

even numbers = [
    number
    for number in numbers
    if number % 2 == 0
]
```

Result:
[2, 4, 6]

## 2.13 Dictionary Comprehensions

We can do the same with dictionaries

```
numbers = [1, 2, 3]
squares = [
    number: number ** 2
    for number in numbers
]
```

Result:
{
1: 1,
2: 4,
3: 9
}

## 2.14 Set Comprehensions

Also possible:

```
numbers = [1, 2, 2, 3, 3, 4]

unique_squares = [
    number ** 2
    for number in numbers
]
```

Result:
{1, 4, 9, 16}

## 2.15 Comprehensin vs Normal Loop

You shouldn't use comprehensions just because they're shorter, cause the code may get complex

```
result = [
    process_user(user)
    for user in users
    if user.is_active
    if user.has_permission
    if user.balance > 10000
]
```

If the logic becomes complicated, a normal loop is often more readable
Interview:
I use comprehensions for simple transformations and filtering. If the logic becomes complex or less readable, I'd use a normal loop

## 2.16 Mutability

A mutable object can be modified afer creation
_numbers = [1, 2, 3]_
_numbers.append(4)_
The list itself changed

An immutable object cannot be modified
_name = "Alice"_
_name.upper()_
This does **not** modify the original string

Instead, it creates a new string
_name = name.upper()_

## 2.17 A Common Interview Trap

```
def add_item(items):
    items.append("new")

my_items = ["a", "b"]

add_item(my_items)

print(my_items)
```

Output:
["a", "b", "new"]

Why?
The function recieved a reference to the same mutable list object

This leads to an important Python concept:
**Python passes object references by assignment**

Better interview explanation is:
Python passes references to objects. The function recieves a reference to the same object, so mutations to a mutable object can be visible to the caller

## 2.18 Copying lists

Consider:

```
a = [1, 2, 3]
b = a

b.append(4)
print(a)
```

What is _a_?
[1, 2, 3, 4]

Because:
**b = a**
doesn't create a new list
Both names refer to the same object

### Shallow copy

```
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)
```

Now:
[1, 2, 3]
[1, 2, 3, 4]

## 2.19 Choosing the Right Data Structure

**Requirement 1**
You need transactions in chronological order
Use:
_list_
because order matters and you may append transactions

**Requirement 2**
You need unique stock symbols
Use:
_set_
_symbols = {"AAPL", "GOOG", "MSFT"}_

**Requirement 3**
You need:
Stock symbol --(to store)-> current price
Use:
_dict_

```
prices = {
    "AAPL": Decimal("225.40"),
    "GOOG": Decimal("510.20")
}
```

**Requirement 4**
you need to store immutable coordinates
_location = (19.0760, 72.87777)_
A tuple makes sense.

## 2.20

Suppose FastAPI recieves JSON like:

```
{
    "symbol": "AAPL",
    "quantity": 10,
    "price": 225.40
}
At the Python level, this conceptually corresponds to a mapping:
{
    "symbol": "AAPL",
    "quantity": 10,
    "price": 225.40
}
```

FastAPI/Pydantic will later give us much better structured representation than manually manipulating dictionaries

# Part 2 Quiz

Q1 - Conceptual
You have 1 million user IDs and repeatedly need to check:
_if user_id in collection_
would you use a _list_ or _set_?
I would use a set cause the the IDs will be unique and since it will be unique the time complexity will be O(1), while if I had used list over here the time complexity would've been O(n) which would not have been great

"I'd use a set because I repeatedly need membership checks. Set membership is O(1) on average due to hashing, while list membership is O(n), so a set scales much better for a large collection"

Q2 - Predict the output

```
def add_item(items):
    items.append("Python")

languages = ["Java", "C++"]

add_item(languages)
print(languages)
```

What is the output, and why does the function change the original list
["Java", "C++", "Python"] The original lists gets modified cause the python gets appends in the items and the languages cause the languages are first called then the objects/values/data in the add_item is passed into languages

Q3 = write code
Given:
_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]_
Create a new list containing only the squares of even numbers
Expected result:
_[4, 16, 36, 64, 100]_
Use a list comprehension

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]
print(squares)
```

Q4 - Data structure selection
You're building a portfolio backend and need:
_stock symbol -> current price_
For example:
AAPL → 225.40
MSFT → 510.20
GOOG → 202.10
Which python data structure would you use and why?
Also: for the prices themselves, would you prefer _Float_ or _Decimal_ in a financial system?
I would use **dict** because it will store it as a key value pair and I will use decimal so that the decimal precision error doesn't occue
