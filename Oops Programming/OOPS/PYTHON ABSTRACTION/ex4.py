#create abstract class
#named Bankaccount as class 
# contruct owner,balance
#@abs method write deposit method to dposit amount
# withdraw thing but different formula
#get balance is not abstract
#writw sub class inherits with bankaccount class 
#📝 Scenario: A Banking system
from abc import abstractmethod,ABC
print("---Employee Details---")
class BankAccount(ABC):
    def __init__(self,name,age,occupation,balance,accountnumber):
        self.name = name
        self.age = age
        self.balance = balance
        self.occupation = occupation
        self.__accountnumber = accountnumber
    @abstractmethod
    def my_details(self):
        pass
    def my_occupation(self):
        pass
    @abstractmethod
    def account(self):
        pass
    def acc_number(self):
        return self.__accountnumber
   

class EMP1Account(BankAccount):
    
    def my_details(self):
        print(f"Employeename: {self.name}")
        print(f"age: {self.age}")
    def my_occupation(self):
        print(f"Occupation:{self.occupation}")
    def account(self):
        print(f"Current Balance:{self.age}")
    def acc_number(self):
        print(f"AccountNumber: {self.acc_number()}") #private member variable
print('\n')
print('\n')   
class SavingAccount(BankAccount):
    def my_details(self):
        return f"Employeename: {self.name}"
    
    
    
        
    def amount_deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"₹ {amount} is successfully deposited on your account |  CurrentBalance is {self.balance}")
        else:
            print("Invalid Deposits!")
    def withdarw(self,with_amount):
        if 0 < with_amount < self.balance :
            self.balance -= with_amount
            print(f" Withdrawn amount: ₹ {with_amount} | CurrentBalance is : ₹ {self.balance}")
            
        else:
            print("Insuffient balance!")
    def account(self):
        print(f"{self.my_details()}")
        print(f"Age: {self.age}") #
        print(f"Account balance: ₹{self.balance}")
print('\n')

emp1 =  EMP1Account("Vishnu VG",25,"Junior Python developer",1230,22004148034)
emp1.my_details()
emp1.my_occupation()
emp1.balance
emp1sa = SavingAccount("Prakash nayagam DJ",35,'Senior Data anayslt',1341,22001223134)
emp1sa.account()
emp1sa.amount_deposit(39)
emp1sa.balance
emp1sa.amount_deposit(9141)
emp1sa.withdarw(100)