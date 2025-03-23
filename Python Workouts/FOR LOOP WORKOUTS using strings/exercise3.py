balance = 4500
while balance > 0:
    withdrawal = int(input("Enter your withdrawal amount: $"))
    if withdrawal > balance:
        print('Insufficent balance')
    else:
        balance -= withdrawal
        print(f"Your currect balance is ${balance} . Your withdrawal amount is ${withdrawal}")
print("Your balance is zero or negative. No further withdrawals possible.")