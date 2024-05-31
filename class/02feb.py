'''
y =sin (x)

import numpy as np
y= np.sin(x)


type(var)
int
float

string

chr(65 ) = A
ord('n')
ord('.')

isinstance

string concatenation


num1= input("Enter first number : ")
num2= input("Enter second number : ")
result= num1 + num2
print(result)

num1= int(input("Enter first number : "))
num2= int(input("Enter second number : "))
result= num1 + num2
print(result)


print("The result is ", result)

factorial



tuples are unmutable
convert it to set to mutate


graph 
xlim
ylim




import pylab as pl
pl.xlim(-3,3)
pl.plot(x,y,'o')

legend in matplotlib
loc='upperright'



couple pendulum mechanism
oscillations to be avoided in the hanging bridge





'''

import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 10, 200)
y = np.sin(x)
plt.xlim(-8,8)
plt.ylim(-8,8)



plt.scatter(x, y, color='red', marker='x')
plt.title('My first graph')
plt.xlabel('x (fortnights)')
plt.ylabel('y (furlongs)')
plt.grid(True)
plt.show()

