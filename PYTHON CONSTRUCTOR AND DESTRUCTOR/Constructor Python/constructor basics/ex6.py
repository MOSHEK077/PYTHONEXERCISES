class Test :
    def __init__(self,t1):
        self.t1 = t1
        
    def display(self):
        if self.t1 >= 90:
            print("Grade A")
        elif self.t1 >= 75:
            print("Grade B")
        elif self.t1 > 50:
            print("Grade C")
        elif self.t1 < 35 :
            print("No Grade Failed!")
        else:
            print("Invalid")
stu1 = Test(98)
stu1.display()
mark2 = Test(56)
mark2.display()
mark3 = Test(34)
mark3.display()
mark4 = Test(86)
mark4.display()