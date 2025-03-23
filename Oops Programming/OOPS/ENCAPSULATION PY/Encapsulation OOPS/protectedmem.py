class Protected:
    def __init__(self):
        self._name = "Jacob"
        self._age = 34
        self._education = "Enginer"
        #protect attribute
class Second(Protected):
    def display_age(self):
        print(self._age)
obj = Second()
obj.display_age()

class Third(Protected):
    def display_name(self):
        print(self._name)
obj2 = Third()
obj2.display_name()

class Fouth(Protected):
    def display_education(self):
        print(self._education)
obj3 = Fouth()
obj3.display_education()