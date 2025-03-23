onetuple = ("Apple","Orange","Graphs")
y = list(onetuple)
y.remove("Orange")
onetuple = tuple(y)
print(onetuple)  

#del #this will raise an error because the tuple no longer exists

