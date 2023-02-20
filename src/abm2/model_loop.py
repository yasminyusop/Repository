# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:49:17 2023

@author: gy22fybm
"""

import random
from matplotlib import pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Create a list to store agents
agents = []


"""
initialisation
"""

#initialisation of all agents
agents.append([random.randint(0,99),random.randint(0,99)])


#append list to add more agents
n_agents = 10
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])

print(agents)


"""
Change agents randomly
"""

for i in range(n_agents):
    #x-coordinates
    rn = random.random()
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1

    #y-coordinates
    rn = random.random()
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)


"""
plot 
"""

# Get the coordinates with the largest x-coordinate
lrx = max(agents, key=operator.itemgetter(0))

# Get the coordinates with the smallest x-coordinate
slx = min(agents, key=operator.itemgetter(0))

# Get the coordinates with the largest y-coordinate
lry = max(agents, key=operator.itemgetter(1))

# Get the coordinates with the smallest y-coordinate
sly = min(agents, key=operator.itemgetter(1))

print("lrx slx lry sly", lrx, slx, lry, sly)

# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
plt.scatter(lrx[0], lrx[1], color='red')
plt.scatter(slx[0], slx[1], color='blue')
plt.scatter(lry[0], lry[1], color='yellow')
plt.scatter(sly[0], sly[1], color='green')
plt.show()



