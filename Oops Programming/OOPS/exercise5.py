class Book:
    def __init__(self,title,details):
        self.title = title
        self.details = details
#creating an instance of book
book1 = Book("Python Programming",{"author":"John Doe","Pages":301,"Publications":"True coding world pvt.lmt"})
print(book1.title)
print(book1.details["author"])