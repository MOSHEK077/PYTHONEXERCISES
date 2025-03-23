class My_info :
    def __init__(self,name,age,reg,college,course):
        self.name = name 
        self.age = age
        self.reg = reg
        self.college = college
        self.course = course
my_ins_obj1 = My_info("Moshek Shaju Jones.J",20,2200122,"Scott christian college,Nagercoil".capitalize(),"B.Sc Physics")
my_ins_obj2 = My_info("Paul henry .Y.S ",20,2012033,"mADURAI csi dental college,madurai".capitalize(),"B.D.S")

print("Name   :",my_ins_obj1.name)
print("Age    :",my_ins_obj1.age)
print("Reg.No :",my_ins_obj1.reg)
print("College:",my_ins_obj1.college)
print("course :",my_ins_obj1.course)
print("\n")
print("Name   :",my_ins_obj2.name)
print("Age    :",my_ins_obj2.age)
print("Reg.No :",my_ins_obj2.reg)
print("College:",my_ins_obj2.college)
print("course :",my_ins_obj2.course)



