class Word : 
    def __init__(self, string) : 
        self.string = string
    def __ne__(self, other) : 
        return self.string.lower() != other.string.lower()
w1 = Word("Hello")
w2 = Word("helo")
print(w1!=w2)