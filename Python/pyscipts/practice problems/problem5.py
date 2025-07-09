# Calculates the sum of digits of a user-entered number
a = int(input("Enter your number : "))
sum = 0 
while (a > 0) : 
    m = a % 10 
    sum += m 
    a //= 10
print(f"The sum of digits of the given number is : {sum}")