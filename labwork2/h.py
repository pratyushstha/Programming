s = input("Enter your Roman Numeral : ")
num = 0 
for i in range(len(s) -1): 
    if s[i] == "M": 
        num = 1000 + num
    elif s[i] == "D": 
        num = 500 + num
    elif s[i] == "C": 
        if s[i+1] == "D" : 
            num = 400 + num - 500
        elif s[i+1] == "M" : 
            num = 900 + num - 1000
        else : 
            num = 100 + num
    elif s[i] == "L": 
        num = 50 + num
    elif s[i] == "X": 
        if s[i+1] == "L" : 
            num = 40 + num - 50
        elif s[i+1] == "C" : 
            num = 90 + num - 100
        else : 
            num = 10 + num
    elif s[i] == "V": 
        num = 5 + num
    else:
        if s[i+1] == "V" : 
            num = 4 + num -5
        elif s[i+1] == "X" : 
            num = 9 + num - 10
        else : 
            num = 1 + num
if s[-1] == "I" : 
    num = num + 1
elif s[-1] == "X" : 
    num = num + 10 
elif s[-1] == "C" : 
    num = num + 100
print(num)
