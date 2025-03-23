#Guessing Game : using For loop:
import random
correct_number = random.randint(1,10)
print("Start Guessing the Number ! Now...")
for i in range(10):
    user_number = int(input("Enter the number: "))
    if user_number < correct_number :
        print("Too Low !")
    elif user_number > correct_number:
        print("Too High")
    else:
        print(f"Congratulations You got the Correct number is {user_number}")
else:
    print(f"Sorry ! The correct number was {correct_number}")