class Book :
    def __init__(self, title, page_count) : 
        self.title = title
        self.page_count = page_count
    def __lt__(self, other) : 
        if self.page_count<other.page_count : 
            return self.page_count
        elif self.page_count ==other.page_count : 
            return None
        else : 
            return other.page_count
b1 = ("Harry", 90)
b2 = ("Potter", 91)
print(b1<b2)