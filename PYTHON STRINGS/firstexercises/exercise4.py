#Python String Membership Operators
"""Membership operators are already Discuessed in the operators section. let see with context of string"""

#There are two types of membership operators:
"""in - "in" operator return true if a character or the entire substring is present in the specified string, Otherwise false."""
"""not in - "not in " operator returns true if a character pr entire substring does not exist in the specified string, otherwise false."""
#Example :
str1 = "Moshek"
str2 = "Shaju"
str3 = "Jones"
str4 = "Moshek"

print('Example of in operator :: ')
print(str2 in str1)
print(str3 in str1)
print(str4 in str1)
print()

print(str2 not in str1)
print(str3 not in str1)
print(str4 not in str1)
print()
