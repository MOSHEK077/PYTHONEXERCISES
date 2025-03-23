"""Let's have a look at another scenario,
what happen if we declare the two same constructors in the class."""
class Student:
    def __init__(self):
        print("The First constructor !")
    def __init__(self):
        print("The Second Constructor !")
    def __init__(self):
        print("The Third Constructor !")
st1 = Student()
"""In the above code, the object
st called the second constructor whereas both have the same configuration. 
The first method is not accessible by the st object. Internally,
the object of the class will always call the last constructor
 
if the class has multiple constructors.

Note: The constructor overloading is not allowed in Python."""