"""Counting the number of objects of a class
The constructor is called automatically when we create the object of the class. Consider the following example.

Example"""
class Stduent :
    count = 0 
    def __init__(self):
        Stduent.count = Stduent.count + 1
in1 = Stduent()
in2 = Stduent()
print("The count of student is :",Stduent.count)