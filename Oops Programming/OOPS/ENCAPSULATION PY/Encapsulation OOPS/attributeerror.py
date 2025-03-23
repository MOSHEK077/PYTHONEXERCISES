"""class Private:
    def __init__(self):
        self.__salary = 500130 # private attribute
    def display_sal( ):
        return self.__salary #acess through public method
obj = Private()
print(obj.__salary()) #works
#print(obj.__salary) #Raises Attribute

PS D:\PYTHON\ENCAPSULATION PY> python -u "d:\PYTHON\ENCAPSULATION PY\attributeerror.py"
Traceback (most recent call last):
  File "d:\PYTHON\ENCAPSULATION PY\attributeerror.py", line 7, in <module>
    print(obj.__salary()) #works
          ^^^^^^^^^^^^
AttributeError: 'Private' object has no attribute '__salary'
PS D:\PYTHON\ENCAPSULATION PY> """