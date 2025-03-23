#PYTHON CONSTRUCTOR:


class Myaccount :
    def __init__(self,acc_no,acbal,acc_hol): #this is constructor
        print("Welcome to SBI Bank !")
        self.acc_no = acc_no
        self.acbal = acbal
        self.acc_hol = acc_hol

print("\n")


ac1 = Myaccount(2442800000901,54635.63,"Moshek Shaju Jones.J")

print(f"Account Holder : {ac1.acc_hol} , {ac1.acc_no} , ₹ {ac1.acbal}")
print("\n")
ac2 = Myaccount(2304313495100,5462.42,"Jacob jerish")

print(f"Account Holder : {ac2.acc_hol} , {ac2.acc_no} , ₹ {ac2.acbal}")
print("\n")
ac3 = Myaccount(3240000054213,4526.4,'Arif khan ')
print(f"Account Holder : {ac3.acc_hol} , {ac3.acc_no} , ₹ {ac3.acbal}")