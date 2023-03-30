# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:44:45 2023

@author: gy22fybm
"""

import random
import math
from matplotlib import pyplot as plt
import operator
import time

# Set the pseudo-random seed for reproducibility
random.seed(0)

agents = []
times = []

# A variable to store the number of agents
n_agents = 500

'''Create loop to run for a range of n_agents'''



def process(n_agents):
    n_agents = 500
    for n in range(n_agents,5000,500):
        print(n) 
        
        start = time.perf_counter()
    
        # Initialise agents
        for i in range(n_agents):
            agents.append([random.randint(0, 99), random.randint(0, 99)])
          
        # Move agents
        for i in range(n_agents):
            # x-coordinate
            rn = random.random()
            if rn < 0.5:
                agents[i][0] = agents[i][0] + 1
            else:
                agents[i][0] = agents[i][0] - 1
            # y-coordinate
            rn = random.random()
            if rn < 0.5:
                agents[i][1] = agents[i][1] + 1
            else:
                agents[i][1] = agents[i][1] - 1
           
        # Calculate max distance     
        def get_distance(x0,y0,x1,y1):
            return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
        
        
        def get_max_distance(agents):
            max_distance = 0
            for i in range(len(agents)):
                a = agents[i]
                for j in range(i+1, len(agents)):
                    b = agents[j]
                    distance = get_distance(a[0], a[1], b[0], b[1])
                    max_distance = max(max_distance, distance)
            return max_distance
    
        end = time.perf_counter()
        t = end - start
        return times.append(t)
   
#print("max_distance", get_max_distance(agents))
print(process(500))
       



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


   
