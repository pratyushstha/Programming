# Reverses the digits of a user-entered number
a = int(input("Enter a number : "))
t = ""  
while a != 0:
    m = a % 10 
    t += str(m)  
    a = a // 10  
print("The reversed digit is", int(t))
