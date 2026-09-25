

class Car:
    def __init__(self, brand,model,year):
        self.brand = brand 
        self.model = model
        self.year = year

    def __str__(self):
        return f"Brand = {self.brand}\nModel = {self.model}\nYear = {self.year}"






brand = input("Enter a car brand: ")
model = input("Enter a car moel: ")
year = input("Enter a year: ")

Car_1 = Car("Toyota","Corolla",2020)
Car_2 = Car(brand, model,year)


print(Car_1)
print(Car_2)





