import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
g = 9.81  # gravity
L1 = 1.0  # length of pendulum 1
L2 = 1.0  # length of pendulum 2
m1 = 1.0  # mass of pendulum 1
m2 = 1.0  # mass of pendulum 2

# The equations of motion
def equations(Y, t):
    theta1, z1, theta2, z2 = Y
    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)
    
    theta1_dot = z1
    z1_dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) - (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
    theta2_dot = z2
    z2_dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    
    return theta1_dot, z1_dot, theta2_dot, z2_dot

# Time array
t = np.linspace(0, 10, 250)

# Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt.
Y0 = [np.pi/4, 0, np.pi/2, 0]

# Integrate the ODE using scipy.integrate.
Y = odeint(equations, Y0, t)

# Extract theta1 and theta2
theta1, theta2 = Y[:,0], Y[:,2]

# Convert to Cartesian coordinates
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

plt.plot(x2, y2, 'r')
plt.show()
