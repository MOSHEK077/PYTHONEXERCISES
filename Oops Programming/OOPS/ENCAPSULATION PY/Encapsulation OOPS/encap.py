class Car:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year
    def get_details(self):
        return f"{self.__make} {self.__model} {self.__year}"
    def set_year(self,year):
        if year > 0 :
            self.__year = year
mycar = Car("Toyota","corolla",2020)
print(mycar.get_details())

mycar.set_year(2022)
print(mycar.get_details())

class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.__year = year  # Private attribute

    def get_details(self):
        return f"{self.__year} {self.__make} {self.__model}"

    def set_year(self, year):
        if year > 0:
            self.__year = year

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_details())  # Outputs: 2020 Toyota Corolla

# Attempt to change the year
my_car.set_year(2022)
print(my_car.get_details())  # Outputs: 2022 Toyota Corolla
