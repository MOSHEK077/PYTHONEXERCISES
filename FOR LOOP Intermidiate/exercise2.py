"""Advanced Exercise 2: Prime Numbers - Sample Code
And here's a hint for the second exercise:"""
for num in range(2,101):
    prime = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0 :
            prime = False
            break
    if prime :
        print(num,end= " ")