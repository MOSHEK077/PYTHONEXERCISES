#Global Scope
xyz = 3141 #normal global variable 
def my_func():
    global xyz # local into global..
    xyz = 4224
    
my_func()
print(xyz)