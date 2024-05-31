import numpy as np

# Given matrix
matrix_data = np.array([[5, 0, 0], [1, 2, 1], [1, 1, 2]])

# Forming mass, damping, and stiffness matrices
mass_matrix = np.eye(3)  # Identity matrix as a placeholder for the mass matrix
stiffness_matrix = matrix_data
damping_matrix = np.zeros_like(matrix_data)  # Assuming no damping for simplicity

# Solving the eigenvalue problem
eigenvalues, eigenvectors = np.linalg.eig(np.linalg.inv(mass_matrix).dot(stiffness_matrix))

# Sorting eigenvalues and corresponding eigenvectors
sorted_indices = np.argsort(eigenvalues)
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Displaying the results
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)

