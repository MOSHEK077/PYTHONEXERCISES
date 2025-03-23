#Decimal to Binary: Convert a decimal number to binary using a while loop.
def decimal_to_binary(decimal_num):
    binary = ""
    while decimal_num > 0 :
        remainder = decimal_num % 2
        binary = str(remainder)+binary
        decimal_num = decimal_num // 2
    return binary
binary_num = 54
print(decimal_to_binary(binary_num))