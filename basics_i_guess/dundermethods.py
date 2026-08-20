from typing import Self

class Car:
    def __init__(self, brand:str, horsepower:int) -> None:
        self.brand = brand
        self.horsepower = horsepower

#dunder methods are nothing but double underscore methods, when we can choose how our object should behave with built-in functions
# like str(), len(), etc., if the user uses only print(volvo) it will print the memory location of the object, to avoid that we can use __str__ method,
# by using this we can customize the output when the object is printed/ we can chose what the o/p shows when print(volvo) is used
   
    def __str__(self) -> str: #str dunder method is used 
        return f"{self.brand} with {self.horsepower} horsepower."
    
    def __add__(self, other: Self) -> str: #add dunder method, it is used to add object to our current object
        return f"{self.brand} + {other.horsepower}"
    
    def __add__(self, other: Self) -> str: #add dunder method, it is used to add object to our current object
        return f"{self.brand} + {other.brand}"
    
    def __mul__(self, other: Self) -> str: #mul dunder method, it is used to multiply object to our current object
        return f"{self.brand} * {other.horsepower}"
#there are multiple different dunder methods like __mul__ for multiplication, __sub__ for subtraction, __len__ for length, etc.
#research more about dunder methods to know more about them in use cases

Volvo: Car = Car("Volvo", 200)
print(Volvo)  # Now it will print "Volvo with 200 horsepower." instead of memory location    

BMW: Car = Car("BMW", 450)

print(Volvo + BMW)  # This will print "Volvo + BMW"

print(Volvo * BMW)  # This will print "Volvo * 450"