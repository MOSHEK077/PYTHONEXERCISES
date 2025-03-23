"""We can use nested if statement for situation where we want to check for a secondary condition if the first condition executes
as true .for this we can have an if else statement inside of another if-else statement.lets look at the syntax of a nested if statementsS"""

a = 10# n 
if a >= 20:  # first condition checking...
    print("Condition is true")
else: # if first one is not true then it will turns second conditions
    if a >= 15: #not true
        print("Checking second value")
    else: # final valueS
      print("All conditions are false!")