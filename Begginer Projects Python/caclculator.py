def calculator():
    operation = input("Choose operations : (+,-,*,/,) :")
    n_1 = float(input("Enter a number n1:"))
    n_2 = float(input("Enter a number n2:"))
    
    if operation == "+":
        print(f"Result :{n_1 + n_2}")
    elif operation == "-":
        print(f"Result :{n_1 - n_2 }")
    elif operation == "*":
        print(f"Result :{n_1 * n_2}")
    elif operation == "/":
        print(f"Result :{n_1 / n_2}")
    else:
        print("Invalid Operation !")
calculator()
        