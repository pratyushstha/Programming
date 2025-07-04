#Check if the given number is palindrome or not
a = int(input("Enter a number : "))
b = str(a)
reverse = ""
l = 0 
while(a>0) : 
    l = a % 10
    a //= 10 
    reverse = reverse + str(l)
if b==reverse : 
    print("The given number is palindrome")
else: 
    print("The given number is not palindrome")

