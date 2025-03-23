"""Advanced Exercise 1: Fibonacci Sequence
Write a for loop to generate the first n numbers in the Fibonacci sequence. For example, if n = 10, the sequence should be 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Advanced Exercise 2: Prime Numbers
Write a for loop to print all prime numbers between 1 and 100.

Advanced Exercise 1: Fibonacci Sequence - Sample Code
Here's a hint to get you started:"""
n = 10
a,b = 0,1
for _ in range(n):
    print(a,end=" ")
    a,b =b,a+b