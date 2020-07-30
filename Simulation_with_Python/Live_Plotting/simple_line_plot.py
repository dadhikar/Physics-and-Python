"""
Created on Sat May  9 18:59:33 2020 @author: dadhikar
"""
import sys
from collections import namedtuple
from functools import partial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
line, = ax.plot([], [], c='r', lw=2.0)
x_data = []
y_data = []

def animation_frame(i):
    x_data.append(i)
    y_data.append(0.1*i)
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,


animation = animation.FuncAnimation(fig, func=animation_frame,
                          frames=100, interval=100)

plt.show()