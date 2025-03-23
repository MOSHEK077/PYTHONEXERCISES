""" Real-World Applications
Number Guessing Game
The user guesses a random number between 1 and 10."""
import random 
number = random.randint(1,15)
guess = 0
while guess != number:
    guess = int(input("ENTER THE NUMBER BETWEEN 1 AND 15:"))
    if guess < number :
        print("Too low !")
    elif guess > number:
        print("Too high !")
print(" congratulations,You got the correct answer !")