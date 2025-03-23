"""Step 3: Use Cases of While Loops

#Basic Applications:

Print odd/even numbers within a range.
Calculate the sum of numbers until a specific condition is met.
Intermediate Applications:

Create a simple guess-the-number game."""
#sum of first n number 
#calculate the sum of numbers from 1 to 100
n = int(input("Enter the number :")) #user input
i = 1  # initilization i 
total = 0 # we need this for output 
while i <= n:  # while loops and conditions
    total += i     # increment with the total + i
    i += 1 # i increment to 1 to user input ;n;
print(f"The number 1 to {n} is {total}")  # @ final output calling