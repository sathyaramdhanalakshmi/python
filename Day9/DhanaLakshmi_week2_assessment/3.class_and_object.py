class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        print(f"The title of the book is:{self.title}")
        print(f"The author of book is: {self.author}")
        print(f"The isbn of the book is:{self.isbn}")
        
b=Book("Mahabharatham", "abc", "1990")
b.display()