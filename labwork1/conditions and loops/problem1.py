#Write a program to check whether a number is prime or not

a = int(input("Enter your number"))
count = 0
for i in range(2, a+1) : 
    if a % i == 0 : 
        count +=1
if count == 1 : 
    print("The given number is prime")
else : 
    print("The given number is not prime")