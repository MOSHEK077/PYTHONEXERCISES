"""3. Using continue
Skip Even Numbers
Print odd numbers from 1 to 10"""
#to print the add number with continue statement
#add numbers
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)