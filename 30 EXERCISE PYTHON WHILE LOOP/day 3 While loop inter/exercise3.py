#GCD Calculation: Find the greatest common divisor (GCD) of two numbers using a while loop.
def gcd(a,b):
    while b :
        a,b = b,a % b 
    return a
num1 = 56
num2 = 98
print("The GCD of ,",num1,"and",num2,"is",gcd(num1,num2))