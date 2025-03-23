"""

x = 42  #Global variable 
def global_fun():
    print(x) #Accessing the global variable
global_fun() #outputs: 5

"""


#Exercise2 :

x = 52 #Global variable
def modify_global():
    global x #Declaring  that we want to use the global x
    x = 41  #Modifying the global variable
   
modify_global()
print(x) #outputs : 41