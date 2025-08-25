#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
def Fib(n) : 
    if n == 1 :
        return 0
    elif n == 2 : 
        return 1
    else : 
        return Fib(n-1) + Fib(n-2)
n = int(input("Enter the term you want : "))
print(Fib(n))

# l1 = []
# for i in range(n+1) : 
#     l1.append(Fib(i+1))
# print(l1)