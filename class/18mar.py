import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np
import math

# Ball.py: Isolated ball with Mass and Radius for OOP
class Ball:
    def __init__(self, mass, radius):
        self.m = mass
        self.r = radius
        
    def getM1(self):
        return self.m                  
         
    def getR(self):
        return self.r
        
    def getI1(self):
        return (2.0/5.0)*self.m*(self.r)**2

# Path.py: Parabolic Trajectory of COM for OOP
class Path:
    def __init__(self, v0, theta):
        self.g = 9.8
        self.v0 = v0
        self.theta = theta
        self.v0x = self.v0*math.cos(self.theta*math.pi/180.0)
        self.v0y = self.v0*math.sin(self.theta*math.pi/180.0)
        
    def getX(self, t):
        return self.v0x*t
        
    def getY(self, t):
        return self.v0y*t - 0.5*self.g*t**2

class Baton(Ball, Path):
    def __init__(self, mass, radius, v0, theta, L1, w1):
        Ball.__init__(self, mass, radius)
        Path.__init__(self, v0, theta)
        self.L = L1
        self.w = w1
        
    def getM(self):
        return 2.0*self.getM1()
    
    def getI(self):
        return (2*self.getI1() + 0.5*self.getM()*self.L**2)
        
    def getXa(self, t):
        xa = self.getX(t) + 0.5*self.L*math.cos(self.w*t)
        return xa
        
    def getYa(self, t):
        return self.getY(t) + 0.5*self.L*math.sin(self.w*t)

    def getXb(self, t):
        return self.getX(t) - 0.5*self.L*math.cos(self.w*t)
        
    def getYb(self, t):
        return self.getY(t) - 0.5*self.L*math.sin(self.w*t)

fig = plt.figure(dpi=200) 
axis = plt.axes(xlim=(-3, 25), ylim=(-1, 8)) 
line, = axis.plot([], [], '-r.', lw=1)

def init(): 
    line.set_data([], []) 
    return line,

def animate(i): 
    t = 0.02 * i
    if mybaton.getXa(t) <= 20:
        x = [mybaton.getXa(t), mybaton.getXb(t)]
        y = [mybaton.getYa(t), mybaton.getYb(t)]
        line.set_data(x, y)
        return line,

mybaton = Baton(0.5, 0.4, 15.0, 45.0, 2.5, -22.0)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=101, interval=1, blit=True, repeat=True)
anim.save('baton_animation.mp4', writer='imagemagick', fps=30)

plt.show()
