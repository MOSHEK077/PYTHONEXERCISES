"""### **Problem 3: Swapping Two Variables**
Write a program to swap the values of two variables without using a temporary variable.  
Ask the user for two numbers as input.

**Example Input**:  
`Enter the first number: 10`  
`Enter the second number: 20`  
**Example Output**:  
`After swapping: First number = 20, Second number = 10`
"""
#number swapping

a = int(input('Enter a first number:'))
b = int(input("Enter a second number:"))
a = a + b  # 20 + 50 = 70
b = a - b  # 70 - 50 = 20
a = a - b  # 70 - 20 = 50
print(f"The first number :{a}, The second number: {b}" )

