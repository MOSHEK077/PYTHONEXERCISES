#student data using __init__()
class Stu_profile :
    def __init__(self,name,age,reg,department):
        self.name = name
        self.age  = age
        self.reg  = reg 
        self.department = department
obj1 = Stu_profile("Moshek Shaju Jones.J",20,2200122,"Department of Physics".capitalize())
obj2 = Stu_profile("Ramesh.L",21,2200421,"Department of commerce".capitalize())
obj3 = Stu_profile("Lokesh.F",19,2300312,"Department of English".capitalize())

print("\n")
print("Name : {} ".format(obj1.name))
print("Age  : {} ".format(obj1.age))
print("R.no : {} ".format(obj1.reg))
print("Dept : {} ".format(obj1.department))
print("\n")
print("Name : {} ".format(obj2.name))
print("Age  : {} ".format(obj2.age))
print("R.no : {} ".format(obj2.reg))
print("Dept : {} ".format(obj2.department))
print("\n")
print("Name : {} ".format(obj3.name))
print("Age  : {} ".format(obj3.age))
print("R.no : {} ".format(obj3.reg))
print("Dept : {} ".format(obj3.department))