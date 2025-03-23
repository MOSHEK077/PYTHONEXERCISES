class Car:
    def __init__(self,speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed
    def set_speed(self,speed):
        self.__speed = speed
obj1 = Car("2000CC")
print(obj1.get_speed())
obj1.set_speed("4000cc")
print(obj1.get_speed())
