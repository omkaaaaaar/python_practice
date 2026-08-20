# Mehod is a fn that is defined inside a class
class Car:
    def __init__(self, brand: str, horsepower:int) -> None:  #ts 3 lines are ATTRIBUTES (features of class (CAR in this case))
        self.brand = brand
        self.horsepower = horsepower

    def describe(self) -> None:  #Method 1
        print(f"This car is a {self.brand} with {self.horsepower} horsepower.")    

    def drive(self) -> None: #Method 2
        print(f"The {self.brand} is now driving.")   #self refer to the instance of the brand, in first examle we choose Volvo so, self = Volvo

    def getinfo(self) -> None: #Method 3
        print(f"{self.brand} with {self.horsepower} horsepower.")

Volvo: Car = Car("Volvo", 200)
Volvo.drive()
Volvo.getinfo()
Volvo.describe()

BMW: Car = Car("BMW", 450)
BMW.drive()