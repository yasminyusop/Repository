# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:44:45 2023

@author: gy22fybm
"""

import random
import math
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io

filename = '//ds.leeds.ac.uk/student/student13/gy22fybm/GEOG5990/Repository/data/input/in.txt'
environment, n_rows, n_cols = io.read_data(filename)

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10


# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = n_cols-1
# The maximum y coordinate.
y_max = n_rows-1

# testing the creation of an Agent
#a = af.Agent()
#print("type(a)", type(a))

# Initialise agents
agents = []
for i in range(n_agents):
    agents.append(af.Agent(i, environment, n_rows, n_cols))
    print(agents[i])
print(agents)

# Move agents
for i in range(n_agents):
    # Change agents[i] coordinates randomly
    agents[i].move(x_min, y_min, x_max, y_max)
print(agents)    

# Eat agents
for i in range(n_agents):
    agents[i].eat()
print(agents)

# Use get_distance
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4

def get_distance(x0,y0,x1,y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
print("distance", get_distance(0,0,3,4))

''' get_distance function was defined with x0,y0,y1,y1
and distance equation was simplified into one line '''

#start = time.perf_counter()

def get_max_distance(agents):
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = get_distance(a.x, a.y, b.x, b.y)
            max_distance = max(max_distance, distance)
    return max_distance

print("max_distance", get_max_distance(agents))

#end = time.perf_counter()
#print("Time taken to calculate maximum distance", end - start, "seconds")    

# Plot

plt.imshow(environment)

for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)
plt.show()

