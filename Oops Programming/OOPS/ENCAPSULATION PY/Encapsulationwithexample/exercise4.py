class Parent:
    def __init__(self,name):
        self.name = name
    def _protected_method(self):
        return f"This is a protected method inside {self.name} class"
class Child(Parent):
    def display(self):
        return self._protected_method()\
            
#creating object 
parent_obj = Parent('Parent class')
child_obj =  Child("Child class")

print(child_obj.display())
print(child_obj._protected_method())