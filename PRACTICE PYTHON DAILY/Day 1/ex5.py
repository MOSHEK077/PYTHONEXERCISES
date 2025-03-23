"""## **Problem 5: Sum and Average of Three Numbers**
Write a program to take three numbers as input and calculate their sum and average.

**Example Input**:  
`Enter the first number: 10`  
`Enter the second number: 20`  
`Enter the third number: 30`  
**Example Output**:  
`Sum = 60`  
`Average = 20.0`"""
a = float(input('Enter the first number :'))
b = float(input('Enter a second number:'))
c = float(input("Enter a third number:"))
sum = a + b + c
average = sum / 3
print("Sum = {} ".format(sum))
print("Average : {} ".format(average))