#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:33:58 2024

@author: hagenimanasalomon
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t,y):
    return y**(c)

def y1(t):
    return ((1-c)*t)**(1/(1-c))

def y2(t):
    return -y1(t)
    
y0 = np.array([0.0])
#y0 = np.array([0.0])
tend = 0.2
c=0.5
sol = solve_ivp(f, [0.0, tend], y0)

plt.figure(1)
plt.plot(sol.t, sol.y[0,:], 'b')
plt.plot(sol.t, y1(sol.t), 'r--')
plt.plot(sol.t, y2(sol.t), 'r--')
plt.grid(True)
plt.show()


