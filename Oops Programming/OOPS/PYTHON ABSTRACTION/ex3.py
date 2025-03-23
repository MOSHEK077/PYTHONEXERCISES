#Object oriented Absraction
#definition: Using classes and inheritance to define abstract interfaces that
#hide implementation details.
#Example Abstract classes (ABC) to enforce method implementation in subclass.

from abc import ABC, abstractmethod
import math
class Shapes(ABC):
    def area(self):
        pass
class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

cir = Circle(3)
print(cir.area())
        