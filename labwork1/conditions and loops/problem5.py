# Write a program to find the largest and smallest number in a list entered by the user.
list1 = []
n = int(input("Enter the number of elements in the list"))
for i in range(1,n+1):
    j = int(input("Enter the {i}th element of the list"))
    list1.append(j)
print(list1)
print(max(list1))
print(min(list1))