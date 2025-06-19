import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math
import random
t = 0
n = 3
r = 0.75
angle = 2*np.pi/n
pts = [[np.sin(k*angle), np.cos(k*angle)] for k in range(n)]
# plt.plot([0, 5, 10], [ 0, math.sqrt(75), 0], "ro")
#plt.plot(pts, "ro")

x, y = zip(*pts)
fig = plt.figure()
plt.plot(x, y, "ro")


px, py = 0, 0 # starting point
plt.plot(px, py, "ko")

def animate(frame):
    global px, py # probably a bad idea
    next_direction = np.array(random.choice(pts))
    px = (1 - r)*px + r*next_direction[0]
    py = (1 - r)*py + r*next_direction[1]
    plt.plot(px, py, "ko", markersize="2")
    
ani = FuncAnimation(fig, animate, frames=400, interval=10)
plt.show()