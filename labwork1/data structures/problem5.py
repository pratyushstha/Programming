#Check if the given number is in a set of prime numbers less than 50
a = set()
count = 0 
for i in range(1, 51): 
    for j in range(2, i+1): 
        if i % j == 0 : 
            count += 1
    if count == 1 : 
        a.add(i)
    count = 0
print(sorted(a))
b = int(input("Enter your number"))
if b in a : 
    print("yes")
else : 
    print("no")