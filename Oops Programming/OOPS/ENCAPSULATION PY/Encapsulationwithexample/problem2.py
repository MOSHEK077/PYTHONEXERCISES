class BankAccount:
    def __init__(self,balance,pin):
        self.__balance = balance
        self.__pin = pin
    def change_pin(self,new_pin):
        if 1000 <= new_pin <= 9999:
            self.__pin = new_pin
            print("PIN successfully changed.")
#"""Changes the PIN only if it is a 4-digit number."""
        else:
            print("Invalid PIN.Please enter 4-digit number.")
    def authenticate(self,pin):
        return pin == self.__pin
    def deposit(self,amount,pin):
        if self.authenticate(pin):
            if amount > 0 :
                self.__balance += amount
                print(f"Deposited ₹{amount} . New balance: ₹{self.__balance}")
            else:
                print("Invalid Deposited amount!")
        else:
            print(f"Incorrect Pin.")
    def withdrawn(self,amount,pin):
        if self.authenticate(pin):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn ₹{amount}, New balance: ₹{self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid PIN.")
    def get_balance(self,pin):
        if self.authenticate(pin):
            return self.__balance
          
        else:
            print("Incorrect PIN. Cannot retrieve balance")
            return None
        
acc = BankAccount(1304,1212)
acc.change_pin(1313)
print(acc.get_balance(1313))
acc.deposit(145,1313)