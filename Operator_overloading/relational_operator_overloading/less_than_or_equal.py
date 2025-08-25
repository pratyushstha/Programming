class Temperature : 
    def __init__(self, temperature_value) : 
        self.temperature_value = temperature_value
    def __le__(self, other) : 
        return self.temperature_value<=other.temperature_value
t1 = Temperature(2000000000)
t2 = Temperature(200000000)
print(t1<=t2)