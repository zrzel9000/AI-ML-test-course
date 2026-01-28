import numpy as np

arr = np.array([45, 78, 92, 60, 55])

arr[arr<60] += 5
 
print(arr)

print(np.mean(arr))