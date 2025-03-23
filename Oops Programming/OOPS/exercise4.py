class Employee :
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary if salary > 0 else 0 
#creating instance of employee with negative salary
employee1 = Employee("Dino Abraham",-5000)
print(employee1.salary)