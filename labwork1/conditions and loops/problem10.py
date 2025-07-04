#menu-driven calculator
a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
op = input("Enter your operator of choice(+, -, *, /)")
if op=="+": 
    print(f"{a+b}")
elif op=="-": 
    print(f"{a-b}")
elif op=="*": 
    print(f"{a*b}")
elif op=="/": 
    print(f"{a/b}")
else: 
    print("Invalid operator")
