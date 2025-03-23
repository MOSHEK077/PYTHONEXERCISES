"""

Enclosing Scope:

Variables in the local scope of enclosing functions.

Often seen in nested functions.

"""
def outer_function():
    x = 30
    def inner_fun():
       print(x)
       
    inner_fun()
outer_function()

print("Hello, World!")  # 'print' is a built-in function
