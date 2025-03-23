"""Inheritance allows a class (child) to derive properties 
and behaviors from another class (parent).
It helps in code reusability and maintaining hierarchy"""

#single inheritance
class Universe:
    def display(self):
        print("Sun is a big star!")
class Earth(Universe):
    def show(self):
        print("Earth is a living plant.")
obj1 = Earth()
obj1.display()
obj1.show()