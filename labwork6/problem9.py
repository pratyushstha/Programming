class Person : 
    def __init__(self, name, age) : 
        self.name = name
        self.age = age
    def __str__(self) : 
        return f"{self.name}, {self.age}"
class Address : 
    def __init__(self, street, city, zipcode) : 
        self.street = street
        self.city = city 
        self.zipcode = zipcode
    def __str__(self) : 
        return f"{self.street}, {self.city}, {self.zipcode}"
class Contact : 
    def __init__(self, person, address) : 
        self.person = person
        self.address = address
    def display_contact(self):
        print(f"{self.person}, {self.address}")
p1 = Person("Hari", 39)
a1 = Address("abc", "xyz", 123)
c1 = Contact(p1, a1)
c1.display_contact()