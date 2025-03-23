#Sum of Digits: Use a while loop to calculate the sum of digits of a number.
number = 12345
sum = 0
while number > 0:
    digits = number % 10
    sum += digits
    number = number // 10
print(sum)

number = 123456
sum = 0
while number > 0 :
    digits = number % 10
    sum += digits
    number = number // 10
print(sum)