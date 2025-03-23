#1. Single Inheritance (General Employee -> Manager)
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show_details(self):
        print(f"Employee Name: {self.name} , Salary: {self.salary}")
class Teamleader(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    def show_details(self):
        print(f"TeamLeader Name: {self.name} , Salary:{self.salary} | Bonus: {self.bonus}")
    def show_role(self):
        print(f"{self.name} is a Team Leader.")

leader = Teamleader("David",78000,1300)
leader.show_details()
leader.show_role()

class Developer(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    def show_details(self):
        print(f"Developer Name: {self.name} , Salary : {self.salary} , Bonus : {self.bonus}")
    def show_role(self):
        print(F'{self.name} is a software developer!' )

dev  = Developer("Moshek Shaju Jones.J",78400,4000)
dev.show_details()
dev.show_role()