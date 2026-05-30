# python_for_numericals

## Built-in Functions

#### Functions is a block of code which only has one function, i.e give it input ut will give you output

ex: Print Function; if we will give input it will provide the same input as the output

1. **print**

```
print("Hello World")
```

2. **input** - when we need to take input from the use

```
input("Enter your age")
```

    -once the user enter the age, the programmer will recieve the age as a string not as int, even if the user entered the age in int it will be recieved as str; to solve this we will need to perform type conversion

3. **type** - it is used to detect the data type in the variable

```
a = 3
type(a)
b = 3.5
type(b)
c = True
type(c)
```

4. **int, float, list, tuple**

```
int(5.6)
#float
#str
#list
#tuple
```

o/p 5

5. **abs** - absolute functiom, it is just the modulus we can eaily print absolute value of any digit

```
abs(4)
abs(-4)
abse(-5)
```

o/p 4
o/p 4
o/p 5

6. **pow** - power function, if we pass two int in it then the second int which will be the power to the 1st int,
   ex: pow(2,3) = 2x2x2 = 8; pow(2,-3) = 1/2x2x2 = 1/8 = 0.125

```
pow(2,3)
pow(2,-3)
```

o/p 8
o/p 0.125

7. **min/max** - in this function we pass a iterable(str, list, tupl, sets) the min is used to find the minimum value of the provide iteration, the max is used to find the maximum value

```
min([2,1,3,0])
max([2,1,3,0])
max("kolkata")
```

o/p 0
o/p 3
o/p 't'

8. **round** - this function is used to get the rounded value of value with multiple decimals; ex: 22/7 = 3.142857142...

```
c = 22/7
rount(c)
rount(c,2)
```

o/p 3
o/p 3.14

9. **divmod** - it returns the tuple (x//y, x%y) x//y = x integer divison y, i.e 5 integer division 2 = 2, x mod y = 1

```
divmod(5,2)
```

o/p (2,1)

10. **bin/oct/hex** - we can get all this value (binary, octal, hexadecimal) value by simply using this function

```
bin(4)
oct(4)
hex(4)

```

o/p '0b100'
o/p '0o4'
o/p '0x4'

11. **id** - it is used to return the address of the variable(in which the value is stored) from the memory

```
a = 3
id(a)
```

o/p 14063575839322
(different for every single device)

12. **ord** - it returns the Unicode code point for a one-character string, returns the ASCII Code

```
ord('c')
ord('C')
ord('A')
```

o/p 99
o/p 67
o/p 65

13. **len** - returns the length of the iterable(string, list, sets, dict)

```
len("kolkata")
len([1,2,3])
```

o/p 7
o/p 3

14. **sum** - adds everysingle item in the iterable, assumption is every single item in the inside are numericals

```
sum([1,2,3,4,5])
```

o/p 15

15. **help** - help on built-in functions, give info about the function

```
help('print')
```

o/p xyz...

---

## List Sorting

1. Intro
   Sorting is a fundamental operation in python that allows arranging elelments in a _specific order_ (ascending or descending)

   - Python provides two primary ways to sort lists:
     - **Using sort() method** -> **Modifies** the **original** list in place.
     - **Using sorted() function** -> Returns a **new sorted list** without modifying the original one.

2. Built-in sort() methods
   The .sort()method sorts a list **in place**, meaning the **original** list is **modified** and no new list is created.

```
list_name.sort(key=None, reverse=False)
```

Explaination:

- _*list_name*_ -> The list to be sorted
- _key (optional)_ -> A function that defines the sorting criterion. Default is None (normal sorting).
- _reverse (optional)_ -> If True, sorts in _descending order_; if False, sorts in _ascending order_(default).

3. sorted() function
   The **sorted()** function returns a new sorted list while keeping the original list unchaned.
   To sort a list in descending order, set **reverse=True**.

```
sorted(iterable, key=None, reverse=False)
```

Explaination:

- _iterable_ -> The list (or iterable) to be sorted.
- _key (optional)_ -> Function for custom sorting.
- _reverse (optioal)_ -> If True, sorts in descending order.

4. Custom sorting
   The **Key** parameter in **sort()** and **sorted()** allows us to define custom sorting logic
   This function is applied to each element before sorting.
   Ex. Sort by the length of the characters in a word, etc

5. reverse() Method
   The **.reverse()** method **flips** the order of elements but deos not sort them.

---

## Collection Module

- This is an alternative in python for data types like list, tuples, etc (basically a replacement for list,etc)
- This ia _Powerful_ alternative for the built in data types
- It is more fast than data types and these modules are reliable than the data types
  5 Subparts of the Collection Module:
  - Namedtuple
  - Deque
  - Counter
  - Defaultdict
  - OrderedDict

1. **Namedtuple**
   It is like a normal tuple but there is a added name to the tuple, this is more cleaner than the tuple
   Elements here can be accessed based on the names
   Faster than regular tuples

2. **Deque**
   It is a fast and flexible list

3. **Counter**
   It is used to count the items

4. **Defaultdict**
   It is used to find the default value of the Dictionary

5. **OrderedDict**
   It is used in less than Python 3.7 version
