"""2. Infinite Loop and Break
Exit on Condition
Keep asking for input until the user types "quit"."""
while True : # while condition is true
    user_input = input("Type 'quit' to exit:") #getting the input from the user
    if user_input.lower() == "quit": #if condition checks the condition is true or false if the condition is true
        print("Exiting....") #execute the "exiting ..."
        break # it use to avoid the condition is not execute again 