#You can access tuple items by referring to the index number, inside square brackets
my_tuple = ("mobile","laptops","earphones","bags","Keyboards","electric guitar")
print(my_tuple[3])
print(my_tuple[1:-2])
"""You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

"""
print(my_tuple[2:])
print(my_tuple[:-1])
print(my_tuple[-4:-1])
if "laptops" in my_tuple:
    print("yes ! 'laptops' is in the tuples")
else:
    print("not here!")