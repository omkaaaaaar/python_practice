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
