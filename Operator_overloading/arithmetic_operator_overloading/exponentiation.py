class Growth : 
    def __init__(self, population, rate) : 
        self.population = population
        self.rate = rate 
    def __pow__(self, time) : 
        return Growth(self.population*(1+self.rate/100)**time, self.rate) 
    def __str__(self) : 
        return f"The new population is {self.population}"
p1 = Growth(1, 10)
print(p1.__pow__(50))