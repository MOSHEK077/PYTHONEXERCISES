#. Encapsulation in a Car Class (Using Protected Attributes)
class Car:
    def __init__(self,brand,speed):
        self.brand  = brand
        self._speed = speed #protected member
    def show_speed(self):
        return f"The speed of {self.brand} car : {self._speed}"
   
      
obj1 = Car("Benz",240)
print(obj1.show_speed()) #works fine

#Accessing protected attribute (Not recommended)
print(obj1._speed) #works , but should not be axxessed durectly
print("#works , but should not be accessed durectly")