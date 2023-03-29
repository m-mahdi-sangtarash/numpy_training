import numpy as np

matrix_c = np.array([[2, 4, 2],
              [2, 1, 2],
              [4, 1, -2]])

matrix_v = np.array([15, -5, 0])

x, y, z = np.linalg.solve(matrix_c, matrix_v)

print("x= ", x)
print("x= ", x)
print("x= ", x)
