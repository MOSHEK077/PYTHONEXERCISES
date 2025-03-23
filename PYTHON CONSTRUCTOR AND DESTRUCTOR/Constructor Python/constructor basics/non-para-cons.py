#non-parameterzied constructor
class Employee:
    def __init__(self):
        print("This is non-parameterized constructor")
    def show(self,name):
        print("Hello",name)
empl1 = Employee()
empl1.show("Shaju")
empl1.show("Jones")
