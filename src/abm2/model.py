# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:17:46 2023

@author: yasmi
"""

import random
import math
import matplotlib
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

# Plot the agents
#plt.scatter(agents[0][0], agents[0][1], color='black')
#plt.scatter(agents[1][0], agents[1][1], color='black')
#plt.show()
# Get the coordinates with the largest x-coordinate
#print(max(agents, key=operator.itemgetter(0)))