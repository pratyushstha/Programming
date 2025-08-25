class Stringrepeater: 
    def __init__(self, string) : 
        self.string = string
    def __mul__(self, integer) : 
        concatenated_string = ""
        for i in range(integer) : 
            concatenated_string = self.string + concatenated_string
        return Stringrepeater(concatenated_string)
    def __str__(self) : 
        return f"{self.string}"
s1 = Stringrepeater("hi")
print(s1*5)