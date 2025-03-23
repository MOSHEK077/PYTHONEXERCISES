"""7. Algorithmic Examples
Factorial Calculation
Compute the factorial of a number."""

n = int(input('Enter the number :'))
fact = 1
while n > 0:
    fact *= n 
    n -= 1
print(f"{fact}")
