import matplotlib.pyplot as plt

time = [1, 2, 3, 4, 5, 6]  
distance = [2, 4, 1, 7, 8, 5] 

plt.scatter(time, distance, color='red', marker='x')
plt.title('My first graph')
plt.xlabel('Time (fortnights)')
plt.ylabel('Distance (furlongs)')
plt.grid(True)
plt.show()
