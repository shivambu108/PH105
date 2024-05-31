
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

t = np.linspace(0, 2 * np.pi)
x = t*np.sin(t)
y = t*np.cos(t)

fig, ax = plt.subplots()
l, = ax.plot([0, 2 * np.pi], [-1, 1])

def animate(i):
    l.set_data(t[:i], x[:i],y[:i] )

for i in range(len(x)):
    animate(i)
    plt.pause(0.01)  

plt.show()
