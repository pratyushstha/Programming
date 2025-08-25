#Create a function power(base, exponent=2) that returns the result of base raised to the power of exponent.Demonstrate it with and without the exponent argument.
def power(b, e = 2) : 
    result = 1
    for i in range(e) : 
        result = b * result
    return result
b = int(input("Enter the base : "))
e = int(input("Enter your exponent : "))
print(power(b, e))
print(power(b))