from abc import ABC ,abstractmethod

class Person(ABC):
    def Work(self):
        pass
    def working(self):
        print("Hi it's just for fun")
    
class Student(Person):
    def Work(self):
        print("The Student is Working with the teachers for their college day!")
class Son(Person):
    def Work(self):
        print("Son was always helps his mother everyday")

per = Person()
son = Son()
per.Work()
son.Work()