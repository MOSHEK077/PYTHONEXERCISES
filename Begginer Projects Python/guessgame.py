#This is my second project (Guessing games using python programming)
import random
def guessinggame():
    
    correct_number = random.randint(1,20)
    
    guess = None
    while guess != correct_number:
        
       guess = int(input("Enter a number :"))
       
       if guess < correct_number :
           
          print("The number is too Low ! ")
       elif guess > correct_number :
          print("The number is too High ! ")
       elif guess == correct_number:
          print(f"Congratulation You Got the Correct answer ! Correct number is {guess}")
       else:
          print("Invalid number !!!!!")
guessinggame()
