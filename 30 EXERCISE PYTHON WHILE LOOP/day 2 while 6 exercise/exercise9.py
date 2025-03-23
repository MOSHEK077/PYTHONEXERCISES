#Number Guessing Game: Implement a simple number guessing game using a while loop.
import random
correct_num = random.randint(1,10)
user = int(input("Enter a number between 1 and 10:"))
while user != correct_num:
    if user != correct_num:
        print("Try Again!")
    user = int(input("Enter the number between 1 and 10:"))
print("Congratulation you got the correct Answer !")