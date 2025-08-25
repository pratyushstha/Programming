d = [36.5, 37.0, 39.2, 35.6, 38.7]
f = list(map(lambda x : (x*(9/5))+32, d))
print(f)
f_filtered = list(filter(lambda x : x<=100, f))
print(f_filtered)