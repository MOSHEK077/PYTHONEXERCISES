class Marks:
    math = 100
    
    def __init__(self):
        self.tamil = 78
        self.english = 98
obj1 = Marks()
obj2 = Marks()

obj1.tamil = 88
obj1.english = 98

Marks.math = 97

print("\n")
print("Tamil :",obj1.tamil)
print("English :",obj1.english)
print("Mathematics",obj1.math)
print("\n")
print("Tamil :",obj2.tamil)
print("English :",obj2.english)
print("Mathematics",obj2.math)