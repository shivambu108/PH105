import matplotlib.pyplot as plt
import numpy as np
num_rows = 70

# Define the number of rows

# Generate random data for x, y, and z coordinates
x_data = np.random.rand(num_rows)  # Random x coordinates
y_data = np.random.rand(num_rows)  # Random y coordinates
z_data = np.random.rand(num_rows)  # Random z coordinates

# Combine x, y, and z data into a single array
A = np.column_stack((x_data, y_data, z_data))

# Print the resulting array
print(A)

# # Assuming A is the data array containing N rows and 3 columns
# # A[1:N, 1:3] corresponds to N iterations, and columns are x, y, and z locations respectively

# # Extracting the data for indices 30 to 60
# indices = range(30, 61)  # indices from 30 to 60 inclusive
# x_data = A[indices, 0]  # x locations
# y_data = A[indices, 1]  # y locations
# z_data = A[indices, 2]  # z locations

# # Plotting x versus y
# plt.plot(x_data, y_data, label='x vs y')

# # Plotting x versus z
# plt.plot(x_data, z_data, label='x vs z')

# # Adding labels and legend
# plt.xlabel('X')
# plt.ylabel('Y / Z')
# plt.title('X versus Y and Z')
# plt.legend()

# # Display the plot
# plt.show()




