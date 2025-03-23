#local scope
"""

Variables defined within a function are in the local 

scope and can only be accessed within that function.

"""
"""

def myscope():
    ab = 134 #local scope
    print(ab)
myscope()

"""
#global scope
#variable defined outside any function or class are in the global scope and can 
#can be accesed anywhere in the code
"""
x = 10*10 #global scope variable
def my_function():
    print(x)
my_function()

"""
#GLOBAL VARIABLE
#variables defined outside any function or class are in the global scope and can be 
#accessed anywhere in the code.


"""

f = 100 #global variable
def my_glo():
    print(f)
my_glo()

"""
#4.enclosing scope:
#In the case of nested functions,the outer function's scope is the enclosing scope
#of the inner funtions.
"""

def outer_funt():
    c = 131
    def inner_fun():
        print(c)
    inner_fun()
outer_funt()


"""

#Buit-in scope 
#python has a set of buit-in names,such as len(),range(),etc.These are always
#avaliable in the global namespace.
