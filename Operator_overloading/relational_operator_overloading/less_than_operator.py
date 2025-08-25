class Book :
    def __init__(self, title, page_count) : 
        self.title = title
        self.page_count = page_count
    def __lt__(self, other) : 
        return self.page_count<other.page_count
b1 = Book("Harry", 91)
b2 = Book("Potter", 92)
print(b1<b2)