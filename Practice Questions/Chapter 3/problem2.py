def Palindrome(n) : 
    b = n
    s = 0
    while n>0 :
        r = n % 10
        n //=10
        s = s * 10 + r
    return b == s
print(Palindrome(12321))
