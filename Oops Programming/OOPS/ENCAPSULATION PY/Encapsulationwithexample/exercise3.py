class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance
        
    #getter 
    def get_acc(self):
        return self.__balance
             
    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
            print(F"After Depositing money : {self.__balance}")
        else:
            print("Invalid deposit!")
    def withdrawal(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Balance after withdrawal : {self.__balance}")
        else:
            print("Invalid withdrawal!")
ac1 = BankAccount("Moshek Shaju Jones . J",1304)
print(ac1.get_acc())
print(ac1.account_holder)
ac1.deposit(400)
print(ac1.get_acc())
ac1.withdrawal(100)
print(ac1.get_acc())
print("Thank you for chossing our ATM !")