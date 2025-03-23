#Non keywords
#to modify a variable in the enclosing (non-global)scope ,use the non local keyword
def outer_function():
    x = 13
    def inner_function():
        nonlocal x 
        x = 414
    inner_function()
    print(x)
outer_function()