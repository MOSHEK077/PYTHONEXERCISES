class Add:#super class
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b 
class Sub(Add):
    def __init__(self,a,b):
        super().__init__(a,b)
    def subs(self):
        return self.a - self.b
class Mul(Sub):
    def __init__(self,a,b):
        Sub.__init__(self,a,b)
    def multi(self):
        return self.a * self.b
class Divi(Mul):
    def __init__(self,a,b):
        Mul.__init__(self,a,b)
    def division(self):
        return self.a / self.b

obj = Divi(3,4)
print(obj.add())
print(obj.multi())
print(obj.subs())
print(obj.division())
obj1 = Mul(4,4)
print(obj1.subs())
print(obj1.multi())
