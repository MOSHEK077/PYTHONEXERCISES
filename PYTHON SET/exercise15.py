"""Difference
The difference() method will return a new set that will contain only the 
items from the first set that are not present in the other set."""

set1 = {"Newset","golden set"}
set2 = {"That","is","Not","golden set"}
set3 = set1-set2
print(set3)


"""Note: The - operator only allows you to join sets with sets, 
and not with other data types like you can with the difference() method.

The difference_update() method will also keep the items from the first 
set that are not in the other set,
but it will change the original set instead of returning a new set."""

"""Symmetric Differences
The symmetric_difference() method will keep only the elements 
that are NOT present in both sets."""

set_is_one = {"Facebook","Twitter(x)","Instagram","Windows","Meta"}
set_is_two = {"Facebook","Copilot","Mp3","Windows 11","X","Windows"}
set_total = set_is_one.symmetric_difference(set_is_two)
print(set_total) #good it does'nt return same value or element in a list


set_is_one = {"Facebook","Twitter(x)","Instagram","Windows","Meta"}
set_is_two = {"Facebook","Copilot","Mp3","Windows 11","X","Windows"}
set_total = set_is_one ^ set_is_two #^^^^
print(set_total) #good it does'nt return same value or element in a list
#Set sucessfully finsihed
