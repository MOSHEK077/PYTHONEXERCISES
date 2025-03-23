"""class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()
"""
class Protected:
    def __init__(self):
        self._age = 34 #protected attribute
class Subclass(Protected):
    def display(self):
        print(self._age) #acessiable in subclass
        
obj = Subclass()
obj.display()