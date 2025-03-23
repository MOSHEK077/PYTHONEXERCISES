class Bankaccount:
    def __init__(self,hol,balance):
        self.hol = hol
        self.__balance = balance
    def show(self):
        return self.__balance
    
obj1 = Bankaccount("Shaju",134)
print(obj1.show())