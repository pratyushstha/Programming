import numpy as np

l1 = list(filter(lambda x: int(str(x)[0])**3 + int(str(x)[1])**3 + int(str(x)[2])**3 == x, np.arange(100, 1000)))
print(l1)
