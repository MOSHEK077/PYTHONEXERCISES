def atm_simulation():
    balance = 12481
    pin = "1212"
    print("welcome to the atm!")
    user_pin = input("Enter the PIN:")
    attempt = 0
    while user_pin != pin and attempt < 3 :
        attempt += 1
        print("Incorrect PIN:")
        user_pin = input("Enter the PIN:")
    if user_pin != pin :
        print("Too many fail attempts ,Your Card has been blocked!!!")
        return
    while True:
        print("\nATM Menu:")
        print("1.Check balance:")
        print("2.Deposit Money:")
        print("3.Withdrawn Money:")
        print("4.Exit")
        
        choice = input("Please select an option (1-4):")
        if choice == "1":
            print(f"Your current balance is {balance}")
        elif choice == "2":
            deposit = float(input("Enter your deposit amount:"))
            if deposit > 0 :
                balance += deposit 
                print(f"You have ${deposit} deposited and your new balance is ${balance}")
            else:
                print("Invalid deposit Money!!!!")
        elif choice == "3":
            withdrawn = float(input("Enter the withdrawn Money:"))
            if withdrawn <= balance :
                balance -= withdrawn
                print(f"{withdrawn} has been withdrawl and your new balance is ${balance}")
            else:
                print("Invalid withdrawl Amount!!!")
        elif choice == "4":
            print("Thank you for using ATM ! , Visit you again......")
            break
        else:
            print("Invalid choice .Please select an option (1-4).")
atm_simulation()
    