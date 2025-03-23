#Binary to Decimal: Convert a binary number to decimal using a while loop.def 
def b_t_d(binary):
    decimal_num = 0
    base = 1
    while binary > 0 :
        last_d = binary % 10
        binary = binary // 10
        decimal_num += last_d * base
        base = base * 2
    return decimal_num
binary = 100111
print(b_t_d(binary))
        
    