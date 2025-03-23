class Student:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age #private
    def get_age(self):
        return f"Your age is : {self.__age}"
    def setter_age(self,newage):
        if self.__age > 0 :
            self.__age = newage
        else:
            print("Invalid age!")
#object instance
obj1 = Student("Abdul rahim",31)
print("Name:{}".format(obj1.name))
print(obj1.get_age())
obj1.setter_age(34)
print(obj1.get_age())