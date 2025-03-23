#Factorial Calculation: Calculate the factorial of a number using a while loop.
n = int(input("Enter the number :"))
fact = 1
while n > 1:
    fact *= n
    n -= 1
print(fact)