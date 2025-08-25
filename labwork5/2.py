class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print(f"{self.name} has obtained {self.marks}")
    
s1 = Student("Ram", 100)
s2 = Student("Shyam", 50)
s3 = Student("Gita", 75)
s1.show_details()
s2.show_details()
s3.show_details()