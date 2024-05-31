import matplotlib.pyplot as plt
import numpy as np

# Load the data from the file
frequency, mic1, mic2 = np.loadtxt('filename.txt', delimiter=',', unpack=True)

# Create a new figure
plt.figure()

# Plot the data
plt.plot(frequency, mic1, label='mic1')
plt.plot(frequency, mic2, label='mic2')

# Add labels and title
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Microphone Data')
plt.legend()

# Show the plot
plt.show()

