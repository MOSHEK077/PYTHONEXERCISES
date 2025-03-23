"""Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates."""


#The intersection() method keeps ONLY the duplicates.

#The intersection() method will return a new set, that only contains the items that are present in both sets.


set1 = {"banana","toyato","apple","kiwi"}
set2 = {"beem","ninja hattori","toyato","kiwi fruit"}
set3_inter = set1.intersection(set2)
print(set3_inter) #or

#another method is here!
set1 = {"banana","toyato".upper(),"apple","kiwi fruit"}
set2 = {"beem","ninja hattori","toyato".upper(),"kiwi fruit".upper(),"apple"}
tset = set1 & set2
print(tset)  #verified