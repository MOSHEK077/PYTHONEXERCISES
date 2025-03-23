"""Question 1:
Create a Python class named Library with a non-parameterized constructor 
that prints a message when an instance of the class is created. 
Additionally, define a method named add_book that takes 
two parameters (title and author) and prints the title 
and author of the book. Create an instance of the 
Library class and call the add_book method with appropriate arguments.

Expected Output:
This is a non-parameterized constructor for Library
Book Title: The Great Gatsby
Author: F. Scott Fitzgerald"""

class Library:
    def __init__(self):
        print("This is non-parameterzied constructor! for library")
    def add_book(self,book_name,author_o_book):
        print("Book Title:",book_name)
        print("Author:",author_o_book)
book1 = Library()
book1.add_book("The Great Gatsby","F. Scott Fitzgerald")

"""PS D:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python>                           > python -u "d:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python\Non-para Exercise\qs1.py"
This is non-parameterzied constructor! for library
Book Title: The Great Gatsby
Author: F. Scott Fitzgerald
PS D:\PYTHON\PYTHON CONSTRUCTOR AND DESTRUCTOR\Constructor Python> 
"""
        
    