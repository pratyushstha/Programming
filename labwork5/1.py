class Book: 
    def __init__(self, title, author, price) : 
        self.title = title
        self.author = author
        self.price = price
    def display_info(self) : 
        print(f"{self.title}, {self.author}, {self.price}")
    def update_price(self, new_price) : 
        self.price = new_price
book1 = Book("The Jungle Book", "Ram", 99)
book1.display_info()
book1.update_price(100)
book1.display_info()