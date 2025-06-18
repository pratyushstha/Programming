#Lists are ordered, mutable collection of heterogeneous elements, enclosed within []

l=[10, 20, 30, 40, 50]
print(l[:]) #Default values are 0 and len(l)
print(l[0:len(l)]) #starting value is included and end value is not included, number of terms is given by (end value-starting value)
#Basic list methods
a=[10, 20, 30]
b=[40, 50]
print(a+b) #Concatanates a and b
#print a-b error
#print a*b error
print(a*3) #repeats the list 3 times
print(type(a))
print(dir(a))
l=[] #empty list
l.append("hello") #takes one argument at a time
print(l)
l.append(30)
l.append(40)
l.append("a")
print(l)
l.insert(1, "hi") #shifts other elements to the right
print(l)
a.append(b)
print(a) #appends the actual list inside
a.extend(b)
print(a) #exteneds the list by adding the list elements of the other list
a.pop(0) #removes by index, also returns the value it popped so print(a.pop(0)) would return the element at index 0
print(a)
a.remove([40, 50]) #removes by element(first instance of the element)
print(a)
a.append(10)
a.append(10)
print(a.count(10)) #counts the number of 10's
a.clear() #clears the list
print(a)

#Tuples are ordered, immutable collection of heterogeneous elements, enclosed within (.)
t=('a', 'b', 1, 2)
print(t.index('a'))
l=[]
l.append(t)
print(l) #l is a list of tuples(1 tuple)

#A dictionary is an unordered, mutable collection of key:value pairs, enclosed within {.}.
#Each key in a dictionary is unique, and is used to access its associated value.

d = {'name':'Ram', 'age':22, 'address':'Kathmandu'}
#name, age and address are keys and Ram, 22 and Kathmandu are values
print(type(d)) #<class 'dict'>
r={} #empty dictionary
r[1] = 1 #entry inside the big brackets is key here
r[2] = 4
r[3] = 9
print(r)
print(d)
print(d.get('name')) #prints the value of the key 'name'
print(d.keys()) #prints all the dict keys as list
print(d.values()) #prints all the dict values as list
print(d.items()) #prints all key value pairs as list

#A set is an unordered, mutable collection of unique elements, enclosed within {.}
#It is used to store multiple items in a single variable, where duplicates are automatically removed.

s = {1, 1, 1, 2, 2, 3, 4, 5, 5, 5}
print(s) #prints {1, 2, 3, 4, 5}

#Other way to make sets
k = set("aaabbbbbeeefffgggc")
print(k)
a={1, 2, 3, 4}
b={1, 3, 5}

print(a|b) #union
print(a&b) #intersection 
print(a^b) #symmetric difference/XOR operation
print(a-b) #difference
print(b-a) #difference

print(type(a))
print(dir(a))
