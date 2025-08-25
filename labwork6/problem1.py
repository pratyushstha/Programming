class Student : 
    def __init__(self, name, roll_number, marks) : 
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def display_info(self) : 
        print(f"NAME : {self.name}, ROLL_NUMBER : {self.roll_number}, MAKRS : {self.marks}")

s1 = Student("Ram", 19, 100)
s1.display_info()
