"""Simple Menu System
A text-based menu for user input.

python
Copy code
"""

while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Select options:")
    if choice == "1":
        print("You selected option 1")
    elif choice == "2":
        print("You selected option 2" )
    elif choice == "3":
        print("Programm exiting!")
        break
    else:
        print("Invaild !. try again")
    
