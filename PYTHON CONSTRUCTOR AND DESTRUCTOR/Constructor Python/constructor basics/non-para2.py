"""Question:
Create a Python class named Person with a non-parameterized constructor that 
prints a message when an instance of the class is created. Additionally, define a method named greet 
that takes one parameter 
(name) and prints a greeting message that includes the name. Create an instance of the Person class and call the 
greet method with an appropriate argument."""

class Person:
    def __init__(self):
        print("This is non-parameterized constructor for person")
    def greet(self,name):
        print("Hello, ",name)

per1 = Person()
per1.greet("Shjau")
per2 = Person()
per2.greet("Kumar")
    
    
    
"""This is a non-parameterized constructor for Person
Hello, Alice!"""