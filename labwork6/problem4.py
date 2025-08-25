from abc import ABC, abstractmethod
class Shape(ABC) : 
    @abstractmethod
    def area(self) : 
        print("compulsory implementation huna paryoo")
class Rectangle(Shape) : 
    def __init__(self, length, width) : 
        self.length = length
        self.width = width
    def area(self) : 
        return self.length * self.width
class Circle(Shape) : 
    def __init__(self, radius) : 
        self.radius = radius
    def area(self) : 
        return 3.14 * self.radius * self.radius
# class Triangle(Shape) : 
#     def __init__(self) : 
#         pass #Just trying to instantiate without area() method, throws error
r1 = Rectangle(10, 20)
print(r1.area())
c1 = Circle(10)
print(c1.area())
# t1 = Triangle()