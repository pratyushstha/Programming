# Writing given records in a file called grocery.txt and then reading and displaying from the same file
records = [
{'name':"rice","price":120,"category":"grocery"},
{'name':"sugar","price":220,"category":"grocery"},
{'name':"wheat","price":320,"category":"grocery"},
{'name':"cereal","price":420,"category":"grocery"},
]
f = open("grocery.txt", "w")
f.write("ID\tNAME\tPRICE\tCATEGORY\n")
count = 1
for entry in records : 
    f.write(f"{count}\t{entry['name']}\t{entry['price']}\t\t{entry['category']}\n")
    count +=1
f.close()
f = open("grocery.txt", "r")
lines = f.readlines()
for line in lines : 
    print(line)
f.close()