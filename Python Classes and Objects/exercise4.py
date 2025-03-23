#default values:
class Person:
    def __init__(self,name = "Unknown",age = 0 ):
        self.name = name
        self.age  = age
inst_ance = Person()
print(inst_ance.name,inst_ance.age)