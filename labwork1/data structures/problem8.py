#count the number of times name appears
names = ['a', 'a', 'b', 'c', 'd']
d = {}
for name in names : 
    if name not in d.keys(): 
        d[name]= names.count(name)
print(d)