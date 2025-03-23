#Multiplication Table: Print the multiplication table of a number using a while loop.
i = int(input("Enter the number:"))
j = 1 
while j <= 10:
    print(f"{j}x{i}={i*j}")
    j += 1