#Sum of Series: Calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n using a while loop.
"""def sum_of_series(n): #function calling and declaring.
    sum_series = 0.0 #series value initialization
    i = 1 # value of i is can be initialized
    while i <= n : # while loop is keep running with the condition is while true
        sum_series += 1/i # conditions in variable
        i += 1 # increment the value of "i"
    return sum_series # call the variable to return
n  =  13 # Number of series in the order of sequnences
print(f"The sum of the series of 1 + 1/2 + 1/3 + .........1/ n  is = {sum_of_series(n)}") # call the function and to print the number ............."""

# now we determine the sum of the given series ?
def sum_of_series(n):
    sum_series = 0.0
    i = 1
    while i <= n :
        sum_series += 1 / i
        i += 1
    return sum_series
n = 5

print("Sum of the series 1 + 1/2 + 1/3 + ... 1/",n,"is",sum_of_series(n))