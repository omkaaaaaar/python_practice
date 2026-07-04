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
