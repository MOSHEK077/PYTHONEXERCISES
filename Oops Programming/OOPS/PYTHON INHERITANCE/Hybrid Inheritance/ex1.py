"""Hybrid Inheritance in Python
Hybrid inheritance is a combination of multiple types of inheritance in a single program. It usually involves a mix of single inheritance, multiple inheritance, multilevel inheritance, and hierarchical inheritance.

Example of Hybrid Inheritance
To understand this, let’s take an example where we combine multiple and hierarchical inheritance:"""

class A : #base class
    def method_A(self):
        print("Method in class A")
#derived class inheriting from A
class B(A):
    def method_B(self):
        print("Method in class B")
class C(A):
    def method_C(self):
        print("Method in class C")
class D(B,C):
    def method_D(self):
        print("Method in class D")
        
obj = D()
obj.method_A()
obj.method_D()
obj.method_B()
obj.method_C()
print(D.mro())