import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t,y):
    return y**(1.0/3.0)

def y1(t):
    return ((2.0/3.0)*t)**(3.0/2.0)

def y2(t):
    return -y1(t)
    
y0 = np.array([0.0])
tend = 0.2
sol = solve_ivp(f, [0.0, tend], y0)

plt.figure(1)
plt.plot(sol.t, sol.y[0,:], 'b')
plt.plot(sol.t, y1(sol.t), 'r--')
plt.plot(sol.t, y2(sol.t), 'r--')
plt.show()