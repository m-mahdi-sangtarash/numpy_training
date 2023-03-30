import numpy as np

coeff = np.array([3, 2, -1])
func = np.poly1d(coeff)
print("func root: ", func.r)
print("The value of the function at -2: ", func(-2))
d_func = np.polyder(func, 1)
print("The derivative of the function at point -2: ", d_func(-2))
