"""        ParentClass
        /     |      \
     Child1  Child2  Child3

"""
#parent class 
class Animal:
    def speak(self):
        return "Animal speaks"
#child class 1

class Dog(Animal):
    def speak(self):
        return "Dog barks"
#child 2
class Cat(Animal):
    def speak(self):
        return "Cat meows"
    
#child 3
class Cow(Animal):
    def speak(self):
        return "Cow moos"

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.speak())
print(cat.speak())
print(cow.speak())
