# Part 3: Classes, Objects, **init**, instance attributes/methods, self, inheritance, method overriding, @staticmethod, @classmethod, **repr**,**str**

## 3.1 What is a Class?

A **class is a blueprint**, and an **object is an actual instance created from that blueprint**

Imagine a _User_
The class describes what a user has and can do.

```
class User:
    pass
```

Now create Objects:
_user1 = User()_
_user2 = User()_

_User_ is the class
_user1_ and _user2_ are objects/instances

## 3.2 **init**

Usually, we want every object to start with some data

```
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now:

```
user = User("Omkar", 21)

print(user.name)
print(user.age)
```

Output:
Omkar
21

**What is happening?**
when you write:
_User("Omkar", 21)_
Python creates an object and initializes it using **init**

## 3.3 What is _self?_

This is one of the most common Python OOP interview questions

```
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"
```

When you do:

```
user = User("Omkar")
user.greet()
```

_self_ refers to **that particular object**
So conceptually:
_user.name_
is the object's _name_
**Important**
_self_ is **not a special keyword** in thesame way _class_ or _def_ is
It's a naming convention, although you should always use _self_ for instance methods

## 3.4 Instance attributes

Each object can have its own state

```
class User:
    def __init__(self, name):
        self.name = name

user1 = User("Omkar")
user2 = User("Rahul")

print(user1.name)
print(user2.name)
```

Output:
Omkar
Rahul
_user1.name_ and _user2.name_ are different attributes belonging to different objects

## 3.5 Instance methods

A method is simply a function defined inside a class

```
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Usage:
account = BankAccount(1000)
account.deposit(500)
print(account.balance)

Result:
1500
This is directly relevant to fintech content: an object can encapsulate **state + behavior**

## 3.6 Inheritance

Inheritance allows one class to derive behavior from another

```
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass
```

Now:
_dog = Dog_
_print(dog.speak())_
The _Dog_ inherits _speak()_ from _Animal_

## 3.7 Method overriding

A child class can provide its own implementation

```
class Animal:
    def speak(self)
        return "Some sound"

class Dog(Animal):
    def speak(self)
        return "Woof"
```

Now:
_dog = Dog()_
_print(dog.speak())_
Output:
Woof
This is called method overriding

## 3.8 super()

Suppose the parent has initialization logic

```
class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, permissions):
        super().__init__(name)
        self.permissions = permissions
```

_super()_ lets the child call the parent's implementation
This is important enough to remember:
_super()_ **allows a subclass to access functionality from its parent class**

## 3.9 @staticmethod

A static method doesn't need access to the instance

```
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
```

Call it:
_MathUtils.add(10, 20)_
There is no _self_
Use a static method when the behavior logically belongs to the class but doesn't need instance or class state

## 3.10 @classmethod

A class method recieves the **class itself** as its first argument, conventionally called _cls_

```
class User:
    user_type = "regular"

    @classmethod
    def get_user_type(cls):
        return cls.user_type
```

Call:
_User.get_user_type()_
Think:
instance method -> self -> object
class method -> cls -> class
static method -> neither

## 3.11 **str** vs **repr** ----

These are **dunder methods** ("double underscore" methods)

### \_ _str_ \_

Intended to provide a user-friendly representation

```
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

Then:
_user = User("Omkar")_
_print(user)_

Produces:
Omkar

### \_ _repr_ \_

Intended a provide a more developer-oriented/unambiguous representation

```
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User(name={self.name!r})"
```

Then:
_user = User("Omkar")_
_print(repr(user))_

could produce:
_User(name='Omkar')_

Shortcut:
\_ _ str _ \_ -> human-friendly representation
\_ _ repr _ \_ -> developer/debugging representation

## Part 3 Quiz

q1 What's the difference between"
_self_ and _cls_ in python methods
self is used for instance methods, it is used to call/refer to a specific particular object, if I defined a function "greet" and used self. "The self in the greet function will refer to the greet, it will call itself" -> ❌
"self refers to the instance/object on which the method was called, not the method itself."✅
cls stands for class method the class method receives whole the class(the blurprint) itself as its first argument
the self calls the object and the cls calls the whole class

"self refers to the current instance and is used by instance methods to access that object's attributes and methods. cls refers to the class itself and is used by class methods to access class-level state or behavior."
"self refers to the current instance."
**init** initializes the object's name attribute, and greet() accesses that attribute through self.name.

q2. Predict the output

```
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

user = User("Omkar")
print(user.greet())
```

Hello Omkar, the greet function includes the calling of self.name which is defined in the previous init function, the greet function gets the name from the their, and when the greet function is called in the print it print outs the self message of its function and also attaches the retrieved name from the init function

q3. Code
Create a class called _BankAccount_ with:

- _balance_ initialized in _*init*_
- a _deposit(amount)_ method
- a _withdraw(amount)_ method
  For nowm assume withdrawal is allowed only if there is enough balance

Example
_account = BankAccount(1000)_
_account.deposit(500)_
_account.withdraw(200)_
_print(account.balance)_

```
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
```

q4. Interview conceptual
Explain the difference between
instance method vs class method vs static method
instance method uses self, when self is called it refers to the object
the class method uses cls as a abbreviation for class, when it is called, it brings down the whole class as it's first argument
the static method doesn't use a self or anything it is used when the behavior logically refers to the class but doesn't requires any instance or a class state
"An instance method receives self and operates on a particular object's state. A class method receives cls and operates on class-level state or provides alternative constructors. A static method doesn't receive either self or cls; it's essentially a utility function grouped inside the class because it is logically related to that class."

Part 3 — Key Takeaways
A class is a blueprint; an object is an instance of that class.
self refers to the current instance; cls refers to the class.
@classmethod receives cls; @staticmethod receives neither self nor cls.
super() allows a subclass to access parent-class functionality.
**str** is human-friendly; **repr** is primarily developer/debugging-oriented.
