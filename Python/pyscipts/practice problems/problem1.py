# Prints the multiplication table of a user-entered number from 1 to 10
a = int(input("Enter your number : "))
for i in range(1, 11) : 
    print(f"{a}*{i} = {a*i}")