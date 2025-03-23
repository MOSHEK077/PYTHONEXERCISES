z = 53 #Is a global variable 
def access_modify_global():
    global z
    z += 20
    print(z)
access_modify_global()
print(z)