# Some 3D Shapes of VPython
from vpython import*
from IPython.display import display
graph1 =display(width=1920, height=1080, title='Vpython 3D Shapes', range=10)
sphere(pos=vector(0,0,0), radius=1, color=color.green)
sphere(pos=vector(0,1,-3), radius=1.5, color=color.red)
arrow(pos=vector(3,2,2), axis=vector(3,1,1), color=color.cyan)
cylinder(pos=vector(-3,-2,3), axis=vector(6,-1,5), color=color.yellow)

