#Write a Python program to remove all duplicates from a list and print the unique elements.
list1 = [1, 2, 3, 5,  4, 5, 6, 5, 3]
duplicate_list = []
for element in list1 : 
    if element not in duplicate_list : 
        duplicate_list.append(element)
print(duplicate_list)