#Accepts a list and returns a list with only even numbers
list1 =  []
even_list = []
for i in range(1, 11) :
    print(f"Enter the {i}th element of the list")
    element = int(input(""))
    list1.append(element)
print(list1)
for element in list1 : 
    if element % 2 == 0 : 
        even_list.append(element)
print(even_list)