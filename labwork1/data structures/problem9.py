#remove elements from a list that are also in another list
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [5, 8, 9, 10, 4]
print(set(l1)-set(l2))