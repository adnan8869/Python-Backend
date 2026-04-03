# Magic methods = Dunder methods (double underscore) __init__, __str__, __add__, __mul__ etc.
# They are automatically called when we use certain operators or functions on our objects.
# They allow us to define how our objects behave with respect to these operators and functions.


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Dunder string method
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Book):
            return self.pages > other.pages
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"Key '{key}' not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 239)
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)


print(book1 == book2)
print(book1<book2)
print(book1>book2)
print(book1 + book2)  
print("Harry" in book3)
print(book3["title"])
print(book3["author"])
print(book3["pages"])

