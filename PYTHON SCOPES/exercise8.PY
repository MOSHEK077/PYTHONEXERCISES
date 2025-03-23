#Long varable in Function 
"""def local_varable():
    y = 30
    print(y)
local_varable()"""
#print(y) #Error : y is not defined outside the function

#Exercise Mixing Local and Global variable

z = 52
def mix_scope():
    z = 42
    print(z)
mix_scope()
print(z)