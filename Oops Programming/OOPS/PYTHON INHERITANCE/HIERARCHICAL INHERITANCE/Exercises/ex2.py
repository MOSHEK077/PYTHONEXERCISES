class Vehicle: # parent class
    def __init__(self,brand,wheels): 
        self.brand = brand
        self.wheels = wheels
    
    def vehicle_info(self):
        return f"Brand : {self.brand} | Wheels : {self.wheels}"
    
class Car(Vehicle):#it is the children class of a Vehicle parent class
    def __init__(self,brand,fuel_type):
        super().__init__(brand,4)
        self.fuel_type = fuel_type
    
    def car_info(self):
        return f"{self.vehicle_info()} | {self.fuel_type}"
  
class Bike(Vehicle):#it is the children class of a Vehicle parent class
    def __init__(self,brand,engine_cc):
        super().__init__(brand,2)
        self.engine_cc = engine_cc
    
    def bike_info(self):
        return f"{self.vehicle_info()} | Engine CC : {self.engine_cc}"

class Truck(Vehicle):#it is the children class of a Vehicle parent class
    def __init__(self, brand,fuel_type,load_capacity):
        super().__init__(brand,6)
        self.fuel_type = fuel_type
        self.load_capacity = load_capacity
        
    def truck_info(self):
        return f"{self.vehicle_info()} | FuelType : {self.fuel_type} | loadCapacity: {self.load_capacity}tons"

car = Car("Toyata","Petrol")
bike = Bike("Ninja",150)
truck = Truck("Asokleyland","Petrol",6)
print(car.car_info())
print(bike.bike_info())
print(truck.truck_info())