#User Input Loop: Keep asking the user for a number until they provide a positive number.

number = int(input("Enter the positive integer:"))
while number <= 0:
    print("dont't enter negative number! please try again!")
    number = int(input("Enter the positive integer:"))
print(f"Thank Your number is {number}")