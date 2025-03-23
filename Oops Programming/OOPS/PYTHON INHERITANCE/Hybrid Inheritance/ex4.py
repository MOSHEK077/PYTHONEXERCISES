
class Add:
    def add(self,a,b):
        return a + b
class Sub:
    def sub(self,a,b):
        return a - b
class Multi(Add,Sub):
    def Mul(self,a,b):
        return a * b
class Division(Multi):
    def divi(self,a,b):
        return a / b
    
add = Add()
print(add.add(34,4))

divi = Division()
print(divi.Mul(4,2))
print(divi.add(9,9))
print(divi.sub(425,245))
print(divi.divi(34,7))