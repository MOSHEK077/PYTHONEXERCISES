from abc import ABC,abstractmethod

class Myclass(ABC):
    
    @abstractmethod #you must write this code in below
    def details(self):
        pass
    def myname(self):
        pass
class Modelclass(Myclass):
    def myname(self):
        print('hi my name is shaju')
    def details(self):
        print("My detail can't be updated")
obj = Modelclass()
obj.myname()
obj.details()