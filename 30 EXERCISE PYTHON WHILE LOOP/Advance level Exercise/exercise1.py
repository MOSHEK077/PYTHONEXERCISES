def atm_sumulation():
    balance = 23211
    pin = "1212"
    print("Welcome to the ATM")
    user_pin = input("Enter the PIN:")
    attempt = 0 
    while user_pin != pin and attempt < 3 :
        attempt += 1
        print("Incorrect PIN ,Try again !")
        user_pin = input("Enter the PIN:")
        if user_pin != pin :
            print("Too many fail attempts ,Your carad has been blocked")
            return
        while True :
            print("\nATM Menu:")
            print("1.Check Balance:")
            print("2.Deposit Money:")
            print("3.Withdrawn Money:")
            print("4.Exit.")
            
            choice = input("Select an option (1-4):")
            if choice == "1":
                print(f"Your Current Balance is {balance}")
            elif choice == "2":
                deposit_money = float(input("Enter the Deposit Money :"))
                if deposit_money > 0 :
                    balance += deposit_money
                    print(f"${deposit_money} has been deposited.your new balance is {balance}")
                else:
                    print("Invalid Deposit Money!!!!!!!!!!!!!")
            elif choice == "3":
                withdrawn_money = float(input("Enter the Withdrawn Money:"))
                if withdrawn_money >= balance:
                    balance -= withdrawn_money
                    print(f"{withdrawn_money} has been withdrawn ,Your New Balance is {balance}")
                else:
                    print("Invalid or insuffient balance funds for withdrawl")
            elif choice == "4":
                print("Thank you for using ATM ! Good Bye ! , Have a nice day!")
                break
            else:
                print("Invalid choice . Please select option from (1 to 4):")
                
                
atm_sumulation()