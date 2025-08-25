class Book : 
    def __init__(self, title, author) : 
        self.title = title 
        self.author = author
    def __str__(self) : 
        return f"{self.title} by {self.author}"
b1 = Book("Romeo and Juliet", "William Shakespeare")
print(b1)