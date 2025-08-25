class Time : 
    def __init__(self, hours, minutes, seconds) : 
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __eq__(self, other) : 
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds : 
            return True
        else : 
            return False
t1 = Time(10, 50, 55)
t2 = Time(10, 50, 56)
print(t1 == t2)