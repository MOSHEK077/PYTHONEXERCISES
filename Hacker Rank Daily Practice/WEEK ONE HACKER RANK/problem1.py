"""The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:

123...n

"""

if __name__ == "__main__" :
    n = int(input("Enter a number:"))
    for i in range(1,n+1):
        print(i,end= ",")