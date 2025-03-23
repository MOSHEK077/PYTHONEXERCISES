#Fibonacci Sequence: Generate the first n numbers of the Fibonacci sequence using a while loop.
def gener_fib(n): # function declaration
    fib_seq = [] # declare the list to store the elements
    a,b = 0,1 # a,b initilazation
    count = 0 # count variable initialization
    while count < n : # while loop call and it check the true statement and execute next line
        fib_seq.append(a) # adding the every value of a
        a,b = b,a+b # variable declaration
        count += 1 #increment the counting values
    return fib_seq # return the value of fib_seq
n = 10 # n variable declaration
print(gener_fib(n)) # call the function to print the final statement.