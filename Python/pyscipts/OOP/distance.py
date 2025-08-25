#Calculating the distance between two points 
import math 
class Point : 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other): 
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
x1 = int(input("Enter your first x-coordinate"))
y1 = int(input("Enter your first y-coordinate"))
x2 = int(input("Enter your second x-coordinate"))
y2 = int(input("Enter your second y-coordinate"))
P1 = Point(x1, y1)
P2 = Point(x2, y2)
print("Distance between points:", P1 - P2)
