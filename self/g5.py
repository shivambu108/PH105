import numpy as np

# Define your system of equations coefficients
# For example, let's consider the following system of equations:
# 3*I1 + 2*I2 - 4*I3 = 1
# 2*I1 + 3*I2 + 3*I3 = 2
# 5*I1 - 3*I2 + 2*I3 = 3

# Coefficients of the left-hand side of the equations
A = np.array([[3, 2, -4], [2, 3, 3], [5, -3, 2]])

# Constants on the right-hand side of the equations
b = np.array([1, 2, 3])

# Use numpy's linear algebra solver to solve for [I1, I2, I3]
I = np.linalg.solve(A, b)

print("The solutions are ", I)
