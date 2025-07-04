# Count the number of characters in a string using a dictionary
str = input("Enter your string")
d = {}
for i in str : 
    if i not in d.keys(): 
        d[i] = str.count(i)
print(d)

#m2
s = "kdjfakdjsf"
unique_s = set(s)
d = {}
for i in unique_s :
    d[i] = s.count(i)
print(d)
