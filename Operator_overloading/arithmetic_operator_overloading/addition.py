class Vector : 
    def __init__(self, x, y) : 
        self.x = x
        self.y = y
    def __add__(self, other) : 
        added_x = self.x + other.x
        added_y = self.y + other.y
        return Vector(added_x, added_y)
    def __str__(self) : 
        return f"The added sum is ({self.x}, {self.y})"
v1 = Vector(1, 2) 
v2 = Vector(3, 4)
print(v1 + v2)