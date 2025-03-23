class A:
    def showA(self):
        print("I am class A")
class B(A):
    def showB(self):
        print("I am class B")
class C(A):
    def showC(self):
        print("I am class C")
class D(B,C):
    def showD(self):
        print("I am class D")
        
obj1 = A()
obj1.showA()
obj2 = C()
obj2.showA()
obj2.showC()
obj3 = D()
obj3.showA()
obj3.showB()
obj3.showC()