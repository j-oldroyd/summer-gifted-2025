import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

# Set up initial parameters for THE CHAOS GAME
n = 3  # number of sides
r = .5  # how far along path

# Draw points on the polygon
angle = 2*np.pi/n
pts = [[2*np.sin(k*angle), 2*np.cos(k*angle)] for k in range(n)]

x, y = zip(*pts)
fig = plt.figure()
plt.plot(x, y, "ro")

# Choose a starting point
px, py = 0, 0
plt.plot(px, py, "ko")


# From the starting point, start moving towards one of the vertices of
# the polygon.  Then plot that point, pick another vertex to move
# towards, and continue
def animate(frame):
    """Update Chaos Game animation."""
    global px, py  # probably a bad idea
    next_direction = np.array(random.choice(pts))
    px = (1 - r)*px + r*next_direction[0]
    py = (1 - r)*py + r*next_direction[1]
    plt.plot(px, py, "bo", markersize="1")

# Animate!
anim = FuncAnimation(fig, animate, frames=1000, interval=1)

plt.show()
