### **Problem 2: Area of a Circle**
"""Write a program to calculate the area of a circle. Ask the user for the radius and use the formula:  
`Area = π * r²`.  
Use `math.pi` for the value of π.

**Example Input**:  
`Enter the radius of the circle: 5`  
**Example Output**:  
`The area of the circle is 78.54`"""

#Write a program to calculate the area of a circle. Ask the user for the radius and use the formula:  
radi = int(input("Enter the radius of the circle:"))
are = 3.14 * (radi*radi)
print(f'The area of the circle is {are}')
