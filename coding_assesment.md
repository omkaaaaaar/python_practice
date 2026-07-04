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
    is_palindrome = s.lower() == s[::-1].lower()

    return(first_three, reverse_string, is_palindrom)
```
