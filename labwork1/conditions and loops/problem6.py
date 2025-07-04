#Write a program that accepts 10 integers from the user and counts how many are positive, negative, and zero.
list1 = []
positive = 0
negative = 0
zero = 0
for i in range(1, 11): 
    a = int(input())
    list1.append(a)
for element in list1: 
    if (element>0): 
        positive +=1
    elif(element<0): 
        negative +=1
    else: 
        zero+=1

print("The number of positive, negative and zero numbers in the given list is : ", positive, negative, zero)