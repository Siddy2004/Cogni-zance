# QUESTION-5
import numpy as np

# ADDITION OF TWO NUMPY ARRAYS
print("ADDITION OF TWO NUMPY ARRAYS")
a   = np.array([19,42,63,107])
print("First Array:\n",a)
print()
b   = np.array([25,-36,45,-107])
print("Second Array:\n",b)
print()
sum = np.add(a,b)
print("Sum of given two numpy arrays:\n",sum)
print()
# MULTIPLICATION OF TWO MATRICES
print("MULTIPLICATION OF TWO MATRICES")
m1      = np.array([[3, 7, 11],[9, -2, 3],[2, 6, -10]])
print("First Matrix:")
print(m1)
print()
m2      = np.array([[-12, 1, 1],[8, 4, 3],[5, 13, 14]])
print("Second Matrix:")
print(m2)
product = m1 @ m2
print()
print("Product of given two matrices:")
print(product)