"""Create a Python class named Animal with a non-parameterized 
constructor that prints a message when an instance of the class is created. 
Additionally, define a method named describe that takes two parameters 
(species and name) 
and prints the species and name of the animal. Create an instance of 
the Animal class and call the describe method with appropriate arguments"""

class Animal:
    def __init__(self):
        print("This is non-parameterized constructor for Animal")
    def detail(self,species,name):
        print("Species:",species,"Name:",name)
Animal1 = Animal()
Animal1.detail("Tiger","Shera")
    
    
    
"""This is a non-parameterized constructor for Animal
Species: Tiger
Name: Shera
"""