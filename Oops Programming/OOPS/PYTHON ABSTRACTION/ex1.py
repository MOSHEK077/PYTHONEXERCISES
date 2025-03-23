from abc import ABC ,abstractmethod


class Vehicle(ABC):
    
    @abstractmethod
    def StartEngine(self):
        pass
class Car(Vehicle):
    def StartEngine(self):
        print("Engine stared!")
class Bike(Vehicle):
    def StartEngine(self):
        print("Bike is actively attend subdant break")
obj = Car()
obj2 = Bike()
obj2.StartEngine()
obj.StartEngine()
obj.StartEngine()
