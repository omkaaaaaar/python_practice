# Coding Assessment

---

# Phase 1

## Topic 1: String Slicing, Reversal, Palindrome Check

### 1. String Slicing

A slice means taking a part of a string.
Python uses this syntax:
_string[start:end:step]_
It returns a **new string**. The original string never changes because strings are immutable

**start**: Where to begin
**end**: Where to stop(not included)
**step**: How many positions to move every time.

Ex1:
_text = "Python"_
_print(text[1:4])_
o/p: yth
Why?
Starts at index 1; _y_
Stop before index 4; _o_ is index 4
so it is: yth

Ex2:
_print(text[:4])_
o/p: Pyth
No starting index means -> Start from beginning

Ex3:
_print(text[2:])_
o/p: thon
No ending index means -> Go till the end

Ex4:
_print(text[::2])_
o/p: Pto
Why?
0 -> P
2 -> t
4 -> o

#### Negative Indexing

Instead of counting from left, Python can count from the end
P y t h o n
0 1 2 3 4 5
-6 -5 -4 -3 -2 -1

_print(text[-2])_
o/p: o

### 2. String Reversal

**What is string reversal?**
Reversal means
_Read the string from the last character to the first_
Ex: Python -> nohtyP

**What do we need to reverse?**
We need

- first character becomes last
- last becomes first
  Instead of manually swapping characters, Python slicing can do it in one line

**How?**
_[::-1]_
start = empty; means: start from the end because the step is negative
end = empty; means: go until the begining
step = -1; means: move backwards one character every time

Ex:
_word = "Python"_
_print(word[::-1])_
o/p: nohtyP

#### Question:

**Reverse a string without using slicing**

```
word = "Python"
result = ""

for ch in word:
    result = ch + result

print(result)
```

o/p: nohtyP

_Explaination;_
Iteration 1:
ch = P
result = ch + result
result = "P" + ""
result = P

Iteration 2:
ch = y
result = ch + result
result = "y" + "P"
result = yP
Instead of adding the new character to the end, we're putting it at the front

Iteration 3:
ch = "t"
result = "t" + "yP"
result = tyP

~ly, after Iteration 6, we get: nohtyP

### 3. Palindrome Check

**What is Palindrome?**
A palindrome is a word that reads the same from both directions.
Ex:
madam
Forward:
madam
Backward:
madam
Palindrome ✅

Ex2:
racecar
Forward:
racecar
Backward:
racecar
Palindrome ✅

Ex3:
python
Forward:
python
Backward:
nohtyP
Not same.
Not Palindrome ❌

**How do we check?**
Reverse the string
Compare original with reverserd
If equal: Palindrome
Else: Not Palindrome

Ex:

```
word = "madam"
if word == word[::-1]:
   print("Palindrome")
else:
   print("Not Palindrome")
```

O/p: Palindrome

**Case-insensitive palindrome**
Suppose
_word = "Madam"_
Without changing case
_Madam_
_madaM_
Not Equal.
So convert to lowercase first.
_word = word.lower()_
_print(word = word[::-1]:)_
O/p: True

### Example (covers all three concepts)

```
text = "Python"

# slicing
print(text[1:4])    #yth

# reversal
print(text[::-1])   #nohtyP

# palindrome
word = "Madam"

word = word.lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

o/p:
yth
nohtyP
Palindrome

**CoderByte-style Practice Problem**
Write a function:
_def analyze_string(s):_
that returns a tuple containig:

1. The first 3 characters of the string
2. The reversed string.
3. _True_ the string is palindrome (case-insensitive), otherwise _False_

```
def analyze_string(s):
    first_three = s[:3]
    reverse_string = s[::-1]
    is_palindrome = s.lower() == reverse_string.lower()

    return(first_three, reverse_string, is_palindrome)
```

## Topic 2: String Methods

String methods are built-in functions that help you search, modify, split, or clean strings.
Since strings are immutable, these methoda return a **new string** (except methods like _find()_ and _count()_ that returns numbers)

### 1. count() - Count occurrences

**What does it do?**
Counts how many times a substring or character appears.
_text = "banana"_
_print(text.count("a"))_
_print(text.counf("an"))_
o/p:
3
2

### 2. find() - Find first occurrence

**What does it do?**
Returns the **index of the first occurrence**
If not found, it returns -1 (it does **not** throw an error)
_text = "banana"_
_print(text.find("n"))_
_print(text.find("z"))_
o/p:
2
-1

Difference from _index()_
_text.index("z")_
❌ Raises:
ValueError: substring not found

So in interviews:

- _find()_ -> returns -1
- _index()_ -> raises an exception

### 3. replace() - Replace text

Creates a new string with replacement
_text = "I like Java"_
_new_text = text.replace("Java", "Python")_
_print(new_text)_
O/p:
I like Python
Original string remains unchanged.

### 4. split() - Convert string into a list

Splits a string using a separator.
_text = "apple, mango, banana"_
_fruits = text.split(",")\_O
\_print(fruits)_
O/p:
['apple', 'mango', 'banana']

Default sepearator is whitespace:
_text = "I love Python"_
print(text.split())
o/p:
['I', 'love', 'Python']

### 5. join() - Convert a list into a string

This is the **reverse of** _split()_
The separator comes **before** _.join()_
_words = ["I", "love", "Python"]_
_sentence = " ".join(words)_
_print(sentence)_
o/p:
I love Python

Another ex:
print("-".join(["2026", "07", "05"]))
o/p:
2026-07-05

### 6. strip() - Remove spaces

Removes whitespace from the begining and end
_text = " Python "_
_print(text.strip())_
o/p:
Python
Also available:
_text.lstrip()_ # Left only
_text.rstrip()_ # Right only

### 7. upper()

Converts everything to uppercase
_text = "Python"_
_print(text.upper())_
o/p:
PYTHON

### 8. lower()

Converts everything to lowercase
_text = "PyTHoN"_
_print(text.lower())_
o/p:
python

### Clean Example

```
text = "  Python is Fun  "

print(text.count("o"))    #1
print(text.find("Fun"))   #12
print(text.replace("Fun", "Easy"))    # Python is Easy
print(text.strip())
print(text.upper())    # PYTHON IS FUN
print(text.lower())    # python is fun

words = words.strip().split()
print(words)    # ['Python', 'is', 'Fun']

print("-".join(words))  # Python-is-Fun
```

### CoderByte-Style Practice Problem

Write a function:
_def process_text(s)_
It should return a tuple containing:

1. The string with leading/trailing spaces removed
2. The string is converted to uppercase
3. The number of times "a" appears (case.insensitive)
4. A list of words obtained usinf _split()_
5. A single string where those words are joined with "-"

```
def process_text(s):
    spaces_removed = s.strip()
    uppercase = spaces_removed.upper()
    a_appeared = s.lower().count("a")
    words = spaces_removed.split()
    joined = ("-".join(words))

    return(spaces_removed, uppercase, a_appeared, words, joined)
```

## Topic 3: COunter

### Explanation

- Count how many times each character appears.
- Most common interview methof: _Counter()_ and manual dictionary
- Time complexity: O(n)

### Code Example

```
s = "banana"

# Method 1: Counter
print(Counter(s))    # Counter({'a': 3, 'n': 2, 'b': 1})

# Method 2: Manual Dictionary
fre1 = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# {'b': 1, 'a': 3, 'n': 2}
```

```
freq = {}
for ch in "hello":
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)    #{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### CoderByte

```
def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return (freq)

or else,

def char_frequency(s):
    freq ={}

    for ch in s:
        freq[ch] = freq.get(ch, 0)+1

    return freq
```

## Topic 4: List Comprehension

### Explanation:

- Create, transform, and filter lists in one line
- Syntax: [expression *for* item *in* iterable *if* condition]
- Extremely common in CoderByte
  expression -> _x_ (what to produce)
  variable -> _x_ (current item)
  iterable -> _nums_
  condition -> _x%2 == 0_

### Code Example

```
nums = [1, 2, 3, 4, 5, 6]

# Square every number:
squares = [x*x for x in numbs]
print(squares)

# Keep only even numbers
evens = [x for x in nums if x%2 == 0]
print(evens)

# Square only even numbers
result = [x * x for x in nums if x%2 == 0]
print(result)
```

o/p:
[1, 4, 9, 16, 25, 36]
[2, 4, 6]
[4, 16, 36]

Common Examples:

```
# Convert strings to uppercase
words = ["python", "ai", "coder"]
upper = [w.upper() for w in words]

# Length of every word
lengths = [len(w) for w in words]

# Remove empty strings
data = ["hi', "", "python", "", "ai"]
clean = [s.strip() for s in data]
clean = [x for x in data if x]
```

### Practive Problem

Using list comprehension only:

```
nums = [2, 5, 8, 11, 14, 17]
#create a new list containing only the even numbers multiplied by 10

result = [x * 10 for x in nums if x%2 == 0]
print(result)
```

## Topic 5: Dictionary: get(), items(), loops

### Explanation

- _get()_ avoids _KeyError_ and is used constantly
- _items()_ is the standard way to loop through key-value pairs.
- Most dictionary problems are just counting or iterating
- xyz*.get*()

### Code Example

```
person = {
    "name": "Alice",
    "age": 25
}

# get()
print(person.get("name"))    # Alice
print(person.get("age"))    # 25
print(person.get("city"))    # None
print(person.get("city", "Unknown"))    # Unknown

# Loop through key-value pairs
for key, value in person.items():
    print(key, value)
```

#### Common Patterns

```
# Frequency Counter
freq ={}

for ch in freq:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


# Sum all dictionary values
marks = {
    "Math": 80,
    "Science": 90,
    "English": 85
}

for value in marks.values():
    total += value

print(total)


# Print key and value
student = {
    "name": "Omkar",
    "age": 21,
    "city": "Mumbai"
}

for key, value in student.items():
    print(key, value)
```

### Practice Problem

```
marks = {
    "Math": 80,
    "Science": 95,
    "English": 75
}

# Using .items, print only the subjects with marks greater than or equal to 80

for key, value in marks.items():
    if value >= 80:
        print(key)
```

## Topic 6: Array Addition & Question Marks

### Problem 1: Array Addition

#### Explanation

- Find the largest number.
- Check if **any combination** of the remaining numbers sums to it.
- This is typically solved using recursion/backtracking

```
def array_addition(arr):
    target = max(arr)
    arr.remove(target)

    def dfs(i, total):    # i = current index, total = current sum
        if total == target:
            return True

        if i = len(arr) or total > target:
            return False

        return dfs(i + 1, total + arr[i]) or dfs(i + 1, total)
        #dfs(i+1, total + arr[i]) -> suggests to take the current number in consideration, and add it, and i+1, total + arr[i] means increase index and add the current index value
        #dfs(i + 1, total) -> suggests to skip the value addition

    return dfs(0,0)  # it means start from index 0 and sum 0

print(array_addition([4, 6, 23, 10, 1, 3]))  # True
print(array_addition([5, 7, 16, 1, 2]))   # False
```

### Problem 2: Question Marks

#### Explanation:

- Find every pair of digits that sums to 10.
- There must be exactly 3 _?_ between them
- If any valid pair doesn't have exactly 3 _3_, return _False_.

```
def question_marks(s):
    found = False

    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(i + 1, len(s)):
                if s[j].isdigit():
                    if int(s[i]) + int(s[j]) == 10:
                        found = True
                        if s[i:j].count("?") != 3:
                            return False

    return found

print(question_marks("arrb6???4xxbl5???eee5"))   # True
print(question_marks("aa6?9"))                   # False
```

## Topic 7: Recursion (Only Fibonacci & Factorial)

### Explanation:

- A recursive function calls itself
- Needs a base case to stop
- These are the only recursion patterns commonly asked for freshers

```
# Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))    # 120


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8
```

Memorize:
Factorial: **return n \* factorial(n-1)**
Fibonacci: **return fibonacci(n-1) + fibonacci(n-2)**

github action

react toggle switch

oops

jobs..container
