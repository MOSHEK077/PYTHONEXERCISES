"""Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:"""

"""my_tuple = ("car","bike","motor bike")
(item1,item2,item3) = my_tuple
print(item2)
print(item1)
print(item3)"""

fruits = ("Apple","Orange","Cherry","Stawberry","Raspberry")
(item1,item2,*item3) = fruits
print(item1)  #this is one of the example for python list asterick*
print(item3)   
print(item2)
print("{} {} ".format(item1,item2))
