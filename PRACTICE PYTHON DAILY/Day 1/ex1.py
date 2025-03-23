"""### **Problem 1: Celsius to Fahrenheit Conversion**
Write a program to convert a temperature from Celsius to Fahrenheit using the formula:  
`F = (C * 9/5) + 32`.  
Ask the user for the Celsius temperature as input.

**Example Input**:  
`Enter temperature in Celsius: 25`  
**Example Output**:  
`25°C is 77.0°F`
"""
celsius = int(input("Enter temperature in celsius:"))
fahrenheit = int(input("Enter temperature in fahrenheit :"))
f = (celsius* 9 / 5)+32
c = (fahrenheit - 32 ) * 5 / 9 
print(f"Celsius to Fahrenheit: {f} , Fahrenheit to celsius : {c}")