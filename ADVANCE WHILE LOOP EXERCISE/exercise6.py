#Simple Login System
"""Break out after 3 failed attempts. """
correct_password = "Jon$jon12"
correct_username = "jones007"
attempt = 0
while attempt < 3:
    username = input("Enter your user name:")
    password = input("ENter your passcode:")
    if correct_username == username and correct_password == password:
        print(" Login successfuly ! , * Access Granted *")
    else:
        attempt += 1
        print("Please Enter correct details ! Try again")
else:
    print("Too many fail attempts")
    