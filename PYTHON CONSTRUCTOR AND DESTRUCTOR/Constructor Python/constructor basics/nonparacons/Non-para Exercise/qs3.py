"""Question 3:
Create a Python class named City with a 

non-parameterized constructor that prints a message when an instance of the class is created. Additionally,

 define a method named info that 

takes two parameters (name and population) and prints the name and population of the city. Create an instance of the City class
 and call the info method with appropriate arguments.

Expected Output:
This is a non-parameterized constructor for City
City Name: Tokyo
Population: 37 million

"""
class City:
    def __init__(self):
        print("This is non-parameterzied constructor for City")
    def main(self,name,population):
        print("City Name:",name)
        print("Population:",population)
pop1 = City()
pop1.main("Tokyo","37 million")

"""PS D:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python>                                                                                                                                     > python -u "d:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python\Non-para Exercise\qs3.py"
This is non-parameterzied constructor for City
City Name: Tokyo
Population: 37 million
PS D:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python> 
"""