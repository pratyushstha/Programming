class Person : 
    def __init__(self, name, age) : 
        self.name = name 
        self.age = age
class Employee(Person) : 
    def __init__(self, employee_id, salary, name, age) : 
        self.employee_id = employee_id
        self.salary = salary 
        super().__init__(name, age)
    def display_Employee(self) : 
        print(f"This is {self.name}, who is {self.age}. Their employee id is {self.employee_id} and salary is {self.salary}")
e1 = Employee(12, 34983, "Ram", 54)
e1.display_Employee()