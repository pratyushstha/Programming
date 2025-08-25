class Player : 
    def __init__(self, score) : 
        self.score = score
    def __gt__(self, other) : 
        return self.score > other.score
p1 = Player(500)
p2 = Player(200)
print(p1>p2)