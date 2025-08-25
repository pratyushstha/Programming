#Taking two complex numbers and then adding them 
class Complex:
    def __init__(self, real, complex):
        self.real = real
        self.complex = complex
    def __add__(self, other): 
        return Complex(self.real+other.real,self.complex+other.complex)
    def __str__(self):
         return f"{self.real} + j{self.complex}"
r1 = int(input("Enter the real part of the first complex number"))
c1 = int(input("Enter the imaginary part of the second complex number"))
r2 = int(input("Enter the real part of the second complex number"))
c2 = int(input("Enter the imaginary part of the second complex number"))
num1 = Complex(r1, c1)
num2 = Complex(r2, c2)
print(num1+num2)
