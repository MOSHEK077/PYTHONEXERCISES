class Family:
    def showG(self):
        print("My family")
class Father(Family):
    def showF(self):
        print("I am your father")
class Mother(Family):
    def showM(self):
        print("I am your mother")
class Son(Father,Mother):
    def shows(self):
        print("I am the first son")
class Daughter(Father,Mother):
    def showd(self):
        print(" I am the young daughther")

obj = Daughter()
obj.showd()
obj.showG()
obj.showF()
obj.showM()
obj1 = Son()
obj1.shows()
obj1.showG()
obj1.showF()
obj1.showM()