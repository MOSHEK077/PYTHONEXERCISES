#Collatz Conjecture: Implement the Collatz conjecture sequence using a while loop.
#collatz conjecture: implement the collatz conjecture sequence using a while loop.
def collatz_sequence(n):
    sequence = []
    while n != 1 :
        sequence.append(n)
        if n % 2 == 0 :
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence
n = 19
print(f"The Collatz sequence staring from {n} is : {collatz_sequence(n)}")