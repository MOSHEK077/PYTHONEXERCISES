"""Question 2:
Create a Python class named Movie with a 
non-parameterized constructor that 
prints a message when an instance of the class is created. 
Additionally, define a method named details that takes two parameters 
(title and director) and prints the title and director of the movie.
Create an instance of the Movie class and call the details method with appropriate 
arguments.

Expected Output:
This is a non-parameterized constructor for Movie
Movie Title: Inception
Director: Christopher Nolan"""

class Movie:
    def __init__(self):
        print("This is non-parameterized constructor for Movie !")
    def show(self,title,Director):
        print("Movie Title :",title)
        print("Director:",Director)
firstshow = Movie()
firstshow.show("Inception","Christopher Nolan")
"""PS D:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python>                           > python -u "d:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python\Non-para Exercise\qs2.py"
This is non-parameterized constructor for Movie !
Movie Title : Inception
Director: Christopher Nolan
PS D:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python> 
"""