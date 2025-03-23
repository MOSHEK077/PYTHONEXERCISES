"""6. Nested While Loops"""
#Now i write the code multiplication tables using Nested While loops
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i}x{j}={i*j}")
        j += 1
    print("---"*10)
    i += 1