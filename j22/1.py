import numpy as np
import pandas as pd

lst = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = []

for i in range(min(len(lst), len(lst2))):
    lst3.append(lst[i] + lst2[i])

print(lst3)

arr1 = np.array(lst)
arr2 = np.array(lst2)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

