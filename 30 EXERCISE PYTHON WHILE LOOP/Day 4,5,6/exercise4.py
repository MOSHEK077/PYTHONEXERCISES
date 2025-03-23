#Reverse a Number: Reverse the digits of a number using a while loop.
def reverse_number(n):
    reversed_number = 0
    while n > 0 :
        digits = n % 10
        reversed_number = reversed_number * 10 + digits
        n = n // 10
    return reversed_number
n = 1234567
print(f"The reversed number is {reverse_number(n)}")