#print armstrong numbers between 100 and 999
arm = 0
l = 0
for i in range(100, 1000): 
    b = i
    while(i>0) : 
        l = i % 10 
        arm = arm + l**3
        i //= 10
    if(b == arm): 
        print(b)
    arm = 0
