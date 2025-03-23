"""Join Sets

There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

"""

"""Union
The union() method returns a new set with all items from both sets."""
set1 = {"apple","orange","Graphs"}
set2 = {"laptops","mouse","Green Plant"}
t_set = set1.union(set2)
print(t_set)

"""Union
The union() method returns a new set with all items from both sets."""

#Use | to join two sets:
set1 = {"apple","orange","Graphs"}
set2 = {"laptops","mouse","Green Plant"}
t_set = set1 | set2
print(t_set)

#Joining of multiple set at a same time period
set1 = {"alpha","Beta","Gamma"}
set2 = {1,32,42,42,13}
set3 = {"John","Peter","James"}
mytoset = set1 | set2 | set3#it use for joining more than two set at a same time
print(mytoset)