#print the fibonacci sequence(0, 1, 1, 2, 3, 5...) upto 'n' terms
n = int(input("Enter the number of terms : "))
a = 0 
b = 1 
print(a)
print(b)
for i in range(1, n-1): 
    c = a + b 
    a = b
    b = c
    print(c)