'''What is Encapsulation?
Encapsulation is one of the four fundamental principles of Object-Oriented Programming (OOP). It refers to the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit, called a class. Additionally, it restricts direct access to some of an object's components, which is a way of preventing unintended interference and misuse of the data.

In simpler terms:

Encapsulation is about hiding the internal details of how an object works.

It provides controlled access to the data through methods (getters and setters).

It ensures data integrity by preventing unauthorized modifications.
_________________________________________________________________________________________________________
Why is Encapsulation Important?
Data Protection: Prevents external code from directly accessing and modifying sensitive data.

Flexibility: Allows you to change the internal implementation of a class without affecting the code that uses it.

Reusability: Encapsulated classes can be reused in different parts of a program or in other programs.

Maintainability: Makes code easier to maintain and debug.

How to Achieve Encapsulation?
Encapsulation is achieved using:

Access Modifiers: Keywords like private, protected, and public to control access to class members.

Getters and Setters: Methods to read and modify private attributes.
__________________________________________________________________________________________________________
'''
class BankAccount:
    def __init__(self,ac_holder,balance):
        self.ac_holder = ac_holder
        self.__balance = balance #private
    #getter 
    def get_balance(self):
        return self.__balance
    #setter 
    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
        else:
            print("Invalid Deposit ! ")
    #withdrawn
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Invalid withdrawal !')
ac1 = BankAccount("Moshek Shaju Jones . J",10)
print(ac1.ac_holder)
print(f"Current Balance : {ac1.get_balance()}")
ac1.deposit(1000)
print(f"Balance after depositing Money : ₹".capitalize() ,ac1.get_balance())
ac1.deposit(500)
print(f"Balance after depositing Money : ₹".capitalize() ,ac1.get_balance())
ac1.withdraw(90)
print("Balance after withdrwal: ₹".capitalize(),ac1.get_balance())
