class Recipe : 
    def __init__(self, recipe) : 
        self.recipe = recipe
    def __truediv__(self, n) : 
        for key in self.recipe : 
            self.recipe[key] = self.recipe[key]/n
        return Recipe(self.recipe)
    def __str__(self) : 
        return f"{self.recipe}"
d1 = Recipe({"rice":5, "daal":1, "tarkari":2})
print(d1/5)