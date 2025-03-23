import re
def is_valid_password(password):
    if len(password) < 8 :
       return False
   
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"[a-z]",password):
        return False
    if not re.search(r"[\d]",password):
        return False
    if not re.search(r"[!@#$%^&*]",password):
        return False
    return True
def password_validation():
    while True:
        password = input("Enter a password : ")
        if is_valid_password(password):
            print("Password is Valid !")
            break
        else:
            print("Invalid password !!!! , Please Try again <<<!>>>")
            print("Password must be at least 8 characters long , include both uppercase and lowercase letters,contain at least one digits,and have at least one special character . ")
            
password_validation()