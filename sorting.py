#Sort()

#TODO: Sort the list of strings

fruits = ["banana", "apple", "mango", "grape", "orange"]
print("Original List:", fruits)
#sorting the list
fruits.sort()
print("Sorted List:", fruits)
fruits.sort(reverse=True)
print("Sorted List in Reverse Order:", fruits)

numbers = [5, 10, 22, 45, 19, 29]
print("Numbers before sorting", numbers)
numbers.sort()
print("Numbers after sorting", numbers)
numbers.sort(reverse=True)
print("Numbers after sorting", numbers)



#sorted()

number = [10, 1090, 2230, 40.5, 129, 29]
sort = sorted(number)
print(number)
print(sort)

sort_desc = sorted(number, reverse=True)
print(sort_desc)




# Custom sorting

words = ["apple", "banana", "cherry", "date", "elderberry"]
# Sort by length of the word
words.sort(key=len)
print("Sorted by length:", words)
# Sort by Sorted
sortt = sorted(words, key=len)
print(sortt)

# Sorting based on the last character of the word

def fun(n):
    return n % 10
numbers = [100, 51, 65, 82, 23]
numbers.sort(key=fun)
print("Sorted based on the last character:", numbers)


# Case-Insensitive sorting
lst = ["Mango", "Kiwi", "banana"]
lst.sort(key=str.lower)
print(lst)


# Reverse() method
letters = ["a", "d", "f", "b"]
letters.reverse()
print(letters)