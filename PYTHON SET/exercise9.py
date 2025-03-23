#Python - Add Set Items
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.

this_set = {"Mango","Juice","Orange","Juice"} #it does'nt allow dulipcate elements
this_set.add("Pineapple")
print(this_set)

"""
Add Sets

To add items from another set into the current set, use the #update() method.

Example:

"""

myset = {"Mango","Juice","Orange","Juice"}
new_set = {"This","is","new","set !"}
myset.update(new_set)
print(myset)

myset = {"Mango","Juice","Orange","Juice"}
new_set = ["This","is","new","set !"] #It can add any iterables
myset.update(new_set)
print(myset)

