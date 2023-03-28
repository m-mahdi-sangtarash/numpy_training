import numpy as np

data1 = np.array([[1, 2], [3, 6]])
data2 = np.array([[-3, 5], [9, 5]])

print(np.stack((data1, data2), axis=0))
print("=========================")
print(np.stack((data1, data2), axis=1))