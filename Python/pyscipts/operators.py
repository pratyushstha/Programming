Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#relational operators
# =, !=, >, <, >=, <=
a = 10
b = 10
c = 2.5
a==b
True
a!=b
False
#True and False are boolean values
a>c
True
a>b
False
a>=b
True
#logical operators
a = True
b = False
result = a and b
result
False
result =  a or b
result
True
not a
False
not b
True
False or False
False
False or True
True
a = 2
b = 2
c = 3
a and b
2
a and c
3
a == b
True
b ==c
False
a== b or a==c
True
#check if a=2, b=2 and c=3 represent isosceles triangle
a==b or a==c
True
#Since any one of the two pairs should be equal to be isosceles, the above proves that a, b and c form isoscles triangle
>>> #Triangle can also be equilateral in above case
>>> ((a==b and b!=c) or (b==c and a!=b) or (a==c and a!=c))
True
>>> #only includes isosceles
>>> c=2
>>> ((a==b and b!=c) or (b==c and a!=b) or (a==c and a!=c))
False
>>> #assignment operator
>>> a=10
>>> #increase value of a by 2
>>> a = a+2
>>> a
12
>>> a+=2
>>> a
14
>>> #identity operator
>>> x = 3
>>> y = 2
>>> x is y
False
>>> z = x
>>> z is x
True
>>> #Becaues z and x point to the same memory address
>>> a = [10, 20, 30]
>>> b = a.copy()
>>> a is b
False
>>> b[0]=100
>>> b
[100, 20, 30]
>>> a
[10, 20, 30]
>>> #a and b are not same. b is a copy of a stored in a different memory location
>>> a is not b
True
>>> a = [10, 20]
>>> b = [10, 20]
>>> a is b
False
>>> #membership operator
>>> 'st' in 'student'
True
>>> 10 in [10, 20, 30]
True
