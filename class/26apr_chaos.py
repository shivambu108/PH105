import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

N =1000
L = 9.8
g = 9.8
y = np.zeroes([2])

y[0]= 30 * np.pi/float(180)
y[1] = 0.0

t = np.linspace(0,45,N)

def pendulum (y,t,L,g):
    dydt0 = y[1]
    dydt1 = (-g/float(L)*np.sin(y[0]))
    f= np.array([dydt0,dydt1])
    return f

def pendulum_approx(y,t,L,g):
    dydt0 =y[1]
    dydt1 = (-g/float(L)*(y[0]))
    f = np.array([dydt0,dydt1])
    return f
