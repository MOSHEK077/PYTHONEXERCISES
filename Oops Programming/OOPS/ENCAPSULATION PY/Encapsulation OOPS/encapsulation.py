def all():
    class Car:
        def open_door_and_proceed(self):
            print("Door Opened")
            print("Enter into car and started.")
            self._accesalarate() #call inside of class
        def _accesalarate(self): #protected function
            print("Throttle increased") 
            self.__engine_perform()
        def __engine_perform(self):
            print("Burst inside.")
            print("Car is moving!")
    my_car = Car() 
    my_car.open_door_and_proceed()

all()
