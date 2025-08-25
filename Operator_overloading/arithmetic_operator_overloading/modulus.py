class CircularList : 
    def __init__(self, item_list) : 
        self.item_list = item_list
    def __mod__(self, n) : 
        return CircularList(self.item_list[n%len(self.item_list)])
    def __str__(self) : 
        return f"{self.item_list}"
l1 = CircularList([0, 1, 2, 3, 4])
print(l1.__mod__(10))