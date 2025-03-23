"""### **Problem 4: Simple Interest Calculation**
Write a program to calculate simple interest using the formula:  
`SI = (P * R * T) / 100`.  
Ask the user for the principal amount (`P`), rate of interest (`R`), and time (`T`).

**Example Input**:  
`Enter the principal amount: 1000`  
`Enter the rate of interest: 5`  
`Enter the time (in years): 2`  
**Example Output**:  
`The simple interest is 100.0`
"""

""" **Problem 4: Simple Interest Calculation**
Write a program to calculate simple interest using the formula:  
`SI = (P * R * T) / 100`.  
Ask the user for the principal amount (`P`), rate of interest (`R`), and time (`T`).
"""
p = int(input("Enter the interest Principle amount :"))
r = int(input("Enter rate:"))
t = int(input("Enter term period:"))
simple_interest = p * r *  t / 100
print(f'Simple interest is {simple_interest}')