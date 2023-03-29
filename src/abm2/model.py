# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:17:46 2023

@author: yasmi
"""

import random
import math
from matplotlib import pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Create a list to store agents
agents = []

# Initialise variable x0
#x0 = random.randint(0, 99)
#print("x0", x0)
# Initialise variable y0
#y0 = random.randint(0, 99)
#print("y0", y0)
#agents.append([x0, y0])


#simplify initialisation - this does not define x0,y0
agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1
print(agents)

rn = random.random()
print("rn", rn)
if rn < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
print(agents)


#append list to add (x1,y1)
agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

# Change x1 and y1 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1
print(agents)

rn = random.random()
print("rn", rn)
if rn < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
print(agents)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates.
dx = x0 - x1
# Calculate the difference in the y coordinates.
dy = y0 - y1
# Square the differences and add the squares
ssd = (dx * dx) + (dy * dy)
print("ssd", ssd)
# Calculate the square root
distance = math.sqrt(ssd)
print("distance", distance)

# Get the coordinates with the largest x-coordinate
lx = max(agents, key=operator.itemgetter(0))
print(lx)

# Plot the agents
plt.scatter(agents[0][0], agents[0][1], color='black')
plt.scatter(agents[1][0], agents[1][1], color='black')
plt.scatter(lx[0], lx[1], color='red')
plt.show()



