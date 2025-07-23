def addition(a, b) : #a, b are formal parameters
    res = a + b
    print(f'{a} + {b} = {res}')

addition(2, 3) #actual arguments

def multiplication(x, y) : 
    res = x * y 
    return res #value can be returned

print(multiplication(3, 4))

def increment(a, b) : 
    a += 1
    b += 1
    return a, b #multiple values can be returned

x, y = increment(2, 4)
print(x, y)

#Default arguments in Python

def display(a = 10, b = 20, c = 30) : 
    print(f"a = {a}, b = {b}, c = {c}")

display(2, 3) #a and b are passed but c is not passed so that O/P is : a = 2, b = 3, c = 30

#Keyword arguments in python 

def display(a = 10, b = 20, c = 30) : 
    print(f"a = {a} b = {b} c  = {c}")
display(c = 100, a = -1, b = 10000) #can be passed in any order


#Use of single and double astrisks in python except multiplication and exponentiation(Operator overloading)
def add(*args) : #receives all the values as a tuple
    print(type(args)) #returns <class 'tuple'>
    print(sum(args))
add(2, 3, 4, 5)

def display(**kwargs) : 
    print(type(kwargs))
    print(kwargs)
display(a = 1, b = 2, c = 3)

#Inline functions
#Lambda function is used as inline function in python
x = lambda i:i+2
print(x(2)) #works the same way preprocessor directives

# map() and filter() functions(built-in functions)

#map()
def squ(i) : 
    return(i**2)
l = [2, 3, 4]
print(list(map(squ, l))) #We have to return list() because value is returned as "map object"

x = map(lambda i:i**2, l)
print(list(x))

#filter()
n = list(range(1, 21)) #filter out even numbers from the list
f = filter(lambda i:i%2==0, n) #prints the values for which the given is true
print(list(f))
def prime(num) : 
    count = 1
    for i in range(2, num + 1):
        if num % i == 0 :
            count +=1
    if count == 2 : 
        return True
p = filter(prime, n)
print(list(p))

#Assignment : Understand return() defined in functools library

