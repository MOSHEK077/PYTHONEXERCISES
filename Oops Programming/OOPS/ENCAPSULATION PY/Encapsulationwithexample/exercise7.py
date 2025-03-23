"""Encapsulation in an ATM Class (Using Private Attributes)
"""
class ATM:
    def __init__(self,pin,balance):
        self.__pin = pin #private attribute
        self.__balance = balance #private attribute
    def check_balance(self,enter_pin):
        if self.__pin == enter_pin:
            return f"You balance : {self.__balance} "
        
        else:
            return "invalid pin !"
    def deposit_cash(self,amount):
        self.__balance += amount
        return f"Deposited amount: {amount} ,Your balance: {self.__balance}"
    def withdraw(self,amount):
        self.__balance -= amount
        return f"Withdrawal amount : {amount} ,Your balance: {self.__balance}"
atm1 = ATM(1421,5245)
print(atm1.check_balance(1344))
print(atm1.check_balance(1421))
atm1.deposit_cash(5000)
print(atm1.check_balance(1421))
atm1.withdraw(200)
print(atm1.check_balance(1421))