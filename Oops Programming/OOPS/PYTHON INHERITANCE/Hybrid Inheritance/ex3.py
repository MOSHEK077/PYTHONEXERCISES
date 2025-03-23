#parent class 1 
class Addition:
    def add(self,a,b):
        return a + b
#parent class 2 
class Subtraction:
    def sub(self,a,b):
        return a - b
    
#intermidiate class inhering from add and sub classes

class Multiplications(Addition,Subtraction): #multiple inheritance
    def mul(self,a,b):
        return a * b
    
#Final class inheriting from multiplication
class Calculator(Multiplications): # Hirarchical inheritance
    def divide(self,a,b): 
        if b != 0 :
            return a / b #multi + hirar = hybrid_inheritance
        else:
            return "Division by zero is not allowed"
calc = Calculator()
print("Addition:",calc.add(10,5))
print('Subraction:',calc.divide(51,3))
print("Multipilcation:",calc.mul(5,5))
print("Subtraction:",calc.sub(524,245))