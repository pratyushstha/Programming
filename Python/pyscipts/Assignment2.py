#Lottery Game
import random
original_list = []
for i in range(15):
    original_list.append(random.randint(1, 100))
print(original_list)
list1 = original_list[:5]
list2 = original_list[5:10]
list3 = original_list[10:]
sum1 = sum(list1)
sum2 = sum(list2)
sum3 = sum(list3)
print(f"List 1 sums to {sum1}, List 2 sums to {sum2}, List 3 sums to {sum3}")
sum = [sum1, sum2, sum3]
print(f"{max(sum)} is the greatest")


