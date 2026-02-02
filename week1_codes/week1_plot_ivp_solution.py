import numpy as np
import matplotlib.pyplot as plt

A = 1.5

def y(t):
    return A*np.exp(-t) + 0.5*np.sin(t) - 0.5*np.cos(t)

tend = 20.0
nt   = 100
taxis = np.linspace(0.0, tend, nt)

plt.figure(1)
plt.plot(taxis, y(taxis))
plt.xlabel('Time t')
plt.ylabel('Solution y(t)')
plt.show