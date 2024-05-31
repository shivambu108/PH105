import numpy as np
import matplotlib.pyplot as plt

def euler_method(func, t0, t_end, P0, dt, r, K):
    t = np.arange(t0, t_end, dt)
    P = np.zeros_like(t)
    P[0] = P0
    
    for i in range(1, len(t)):
        P[i] = P[i-1] + func(P[i-1], t[i-1], r, K) * dt
    
    return t, P

def euler_cromer_method(func, t0, t_end, P0, dt, r, K):
    t = np.arange(t0, t_end, dt)
    P = np.zeros_like(t)
    P[0] = P0
    
    for i in range(1, len(t)):
        dPdt = func(P[i-1], t[i-1], r, K)
        P[i] = P[i-1] + dPdt * dt
    
    return t, P

def logistic_growth(P, t, r, K):
    return r * P * (1 - P / K)

# Initial parameters
r = 0.1  # Growth rate
K = 1000  # Carrying capacity
P0 = 100  # Initial population size
t0 = 0    # Initial time
t_end = 50  # End time
dt = 0.1  # Time step size

# Original growth curve
t_original = np.linspace(t0, t_end, 1000)
P_original = K * P0 / (P0 + (K - P0) * np.exp(-r * (t_original - t0)))

# Using Euler's method
t_euler, P_euler = euler_method(logistic_growth, t0, t_end, P0, dt, r, K)

# Using Euler-Cromer's method
t_ec, P_ec = euler_cromer_method(logistic_growth, t0, t_end, P0, dt, r, K)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_original, P_original, label='Original', color='black')
plt.plot(t_euler, P_euler, label="Euler's Method", linestyle='--', marker='o', markersize=3, color='blue')
plt.plot(t_ec, P_ec, label="Euler-Cromer's Method", linestyle='--', marker='s', markersize=3, color='red')

plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Population Growth')
plt.legend()
plt.grid(True)
plt.show()

