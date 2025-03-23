"""4. While Loop with Else
Verify All Numbers Are Positive
Check if all numbers in a list are positive."""
list = [42,24,24,52,42,313,-24,424,-42]
i = 0
while i < len(list):
    if list[i] < 0:
        print("List contains negative numbers")
        break
    i += 1
else:
    print("All are positive integers")
    