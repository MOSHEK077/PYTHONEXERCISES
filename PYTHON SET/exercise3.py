"""Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:"""
new_set = {"Welcome","To","the","Home",True,1,2} #True = 1 in a set
print(new_set)

"""PS D:\PYTHON\PYTHON SET> python -u "d:\PYTHON\PYTHON SET\exercise3.py"
{True, 'the', 2, 'Home', 'Welcome', 'To'}
PS D:\PYTHON\PYTHON SET> 

"""

another_set = {"Neem Tree","James Book","Rain",False,True,0,2}  #False = 0 in a set
print(another_set)

#{False, 1, 2, 'Rain', 'James Book', 'Neem Tree'}......
print(len(another_set)) #Length of the given list......
