class Car:
    def __init__(self,no_wheels,mileage,airbags):#Constructor: 
        print("This is constructor!")
        self.mileage = mileage
        self.no_of_wheels = no_wheels
        self.no_of_airbags = airbags
    def moveForward(self,speed):
        print(f"Car is moving with speed of {speed} km")
    def moveBackward(self):
        print("Car is moving backward !")
car1 = Car(4,24.3,1) #Creation of instance
print(car1.mileage,car1.no_of_wheels,car1.no_of_airbags)
