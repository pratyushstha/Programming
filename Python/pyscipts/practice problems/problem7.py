# Splits 10 random numbers into even and odd lists and prints both lists and their counts

import random
a = []
even_list = []
odd_list = []
for i in range(1, 11): 
    a.append(random.randint(1, 100))
for j in a:
    if (j%2 ==0): 
        even_list.append(j)
    else : 
        odd_list.append(j)
print(odd_list)
print(even_list)
count_odd = 0
for i in odd_list: 
    count_odd+=1
print(count_odd)
count_even=0
for i in even_list: 
    count_even+=1
print(count_even)