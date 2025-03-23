"""The __init__() Function:

The examples above are classes and objects in their simplest form,

and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__()

function.


All classes have a function called __init__(),

which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties,

or other operations that are necessary to do when the object is being created:"""

class Peson:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
to_per = Peson("JOHN".capitalize(),24) #obj

print(to_per.name)
print(to_per.age)
print("\n")
ano = Peson("Shaju",20) #obj
print(ano.name)
print(ano.age)
"""Note: The __init__() function is called ,

automatically every time the class is being used to create a new object."""