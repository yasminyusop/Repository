# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:44:45 2023

@author: gy22fybm
"""

import random
import math
import matplotlib
from matplotlib import pyplot as plt
import operator
import time

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 1000
n_iterations = 1000

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99

# Initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
#print(agents)

# Move agents
# Apply movement constraints.
for i in range(n_iterations):
    if agents[i][0] < x_min:
        agents[i][0] = x_min
    if agents[i][1] < y_min:
        agents[i][1] = y_min
    if agents[i][0] > x_max:
        agents[i][0] = x_max
    if agents[i][1] > y_max:
        agents[i][1] = y_max
    
    for i in range(n_agents):
        # Change agents[i] coordinates randomly
        # x-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][0] = agents[i][0] + 1
        else:
            agents[i][0] = agents[i][0] - 1
        # y-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][1] = agents[i][1] + 1
        else:
            agents[i][1] = agents[i][1] - 1
#print(agents)


# Plot
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()

"""
start of abm3
"""
# Use get_distance
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4

def get_distance(x0,y0,x1,y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
print("distance", get_distance(0,0,3,4))

''' get_distance function was defined with x0,y0,y1,y1
and distance equation was simplified into one line '''

start = time.perf_counter()

def get_max_distance(agents):
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            max_distance = max(max_distance, distance)
    return max_distance

print("max_distance", get_max_distance(agents))

end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")    