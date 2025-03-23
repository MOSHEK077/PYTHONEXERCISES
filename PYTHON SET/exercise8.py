#accesing the set items 
#using for loop
myset =  {"Laptops","Mobiles","TVs"}
for c in myset:
    print(c)
print("banana" in myset)
print("Laptops" in myset)
print("Laptops" not in myset)
print("apple" not in myset)
print("TVs"not in myset)
print("TVs" in myset)
print("Mobiles" in myset)
print("Laptops Gadgets" in myset)

"""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop,
or ask if a specified value is present in a set, by using the in keyword.

"""