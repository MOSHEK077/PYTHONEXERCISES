#Prime numbers: Print all prime numbers between 1 and 100 using a while loop

def is_prime(num):
    if num <= 1 :
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
        return True
def print_prime():
    num = 2
    while num <= 100:
        if is_prime(num):
            print(num)
        num += 1
print_prime()

