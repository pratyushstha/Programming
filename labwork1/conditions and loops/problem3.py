#Write a program that reads a number and prints the factorial of that number using a while loop.

a = int(input("Enter your number"))
fact = 1
while(a!=1): 
    fact = fact*a
    a = a - 1
print("The factorial of the given number is", fact)
