#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.

thisset = {"Mouse","Monitor","Keyboard","Windows"}
thisset.discard("Mouse")
print(thisset)
thisset.remove("Monitor")
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
"""You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

Example"""
thisset.clear()
print(thisset)
del thisset #The del keyword will delete the set completely:

print(thisset)