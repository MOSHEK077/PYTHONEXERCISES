"""In Python, multilevel inheritance is a type of inheritance where a class is derived from a class that is also a derived class.
In simpler terms, 
it involves a chain of classes where each class inherits from the class directly above it. 
This creates a multi-level hierarchy of classes."""

class Superclass:
    def supercls(self):
        print("We are inside in Superclass")
class Derivedcls1(Superclass) :
    def derived1(self):
        print("We are indside in a Derived class 1")
class Derived2(Derivedcls1):
    def derived2(self):
        print("We are inside in a Derived class2")
obj = Derived2()
obj.derived1()
obj.supercls()
obj.derived2()