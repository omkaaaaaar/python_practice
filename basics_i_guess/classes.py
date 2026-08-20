#a class is just a blueprint for code organization
#class is used to simplify the process of crating multiple objects with similar attributes, easy for duplication of code
class Car:  #the first letter of class name is always capital
    def __init__(self, brand:str, color:str, horsepower:int): #an initializer is used define and initialize the attributes of the class,  attributes(features) are the variables the belong to the class(car in this case)
        if horsepower <= 0:
            raise ValueError("Horsepower must be a positive integer.")
        self.brand = brand
        self.color = color #in the __init__ method, self allows us to assign value to the instance's attributes
        self.horsepower = horsepower
#ts above is the blueprint of how the car should look
    def describe(self): 
        print(f"This car is a {self.brand} with {self.horsepower} horsepower in {self.color} color.")
#THE above snippet is used to add description

#car number 1
volvo: Car=Car("Volvo","Blue", 200)  #creating an instance of the class Car, volvo is an object of class Car
volvo.describe()
print(volvo.brand)
print(volvo.color)
print(volvo.horsepower)
#car number 2
BMW: Car=Car("BMW","Red", 450)
print(BMW.brand)
print(BMW.horsepower)
print(BMW.color)