# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:44:45 2023

@author: gy22fybm
"""

import random
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as gy
import imageio
import os
import matplotlib.animation as anim

filename = '//ds.leeds.ac.uk/student/student13/gy22fybm/GEOG5990/Repository/data/input/in.txt'
environment, n_rows, n_cols = io.read_data(filename)

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Function definitions
# Function to calculate max distance
def get_max_distance(agents):
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = gy.get_distance(a.x, a.y, b.x, b.y)
            max_distance = max(max_distance, distance)
    return max_distance

# Function that adds up all the store values in all agents
def sum_agent_stores():
    r = 0
    for a in agents:
        r = r + a.store
    return r

# Function that adds up all the values in the environment
def sum_environment():
    r = 0
    for row in environment:
        r = r + sum(row)
    return r

# Plotting code block changed into a function that defines the plot
def plot():
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
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
    global ite
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    images.append(imageio.imread(filename))
    plt.show
    return fig


# Create directory to write images to.
try:
    os.makedirs('../../data/output/images/')
except FileExistsError:
    print("path exists")

# For storing images
global ite
ite = 1
images = []


# Change the model loop code block into a function
def update(frames):
    # Model loop
    global carry_on
    #for ite in range(1, n_iterations + 1):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    # Print the total amount of resource
    sum_as = sum_agent_stores()
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))

    # Stopping condition
    # Random
    if random.random() < 0.1:
        #if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")

    # Plot
    plot()


def gen_function():
    global ite
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (ite <= n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Write data
        print("write data")
        io.write_data('../../data/output/out7.txt', environment)
        imageio.mimsave('../../data/output/out7.gif', images, fps=3)
        data_written = True

# Initialise variables
n_agents = 10
n_iterations = 10
neighbourhood = 20

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = n_cols-1
# The maximum y coordinate.
y_max = n_rows-1

# Initialise agents
agents = []

for i in range(n_agents):
    agents.append (af.Agent(agents, i, environment, n_rows, n_cols))
    print(agents[i])

# Test if code works by printing one agent from another
print(agents[0].agents[1])


# Animate
# Initialise fig and carry_on
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
data_written = False
animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)



    


#imageio.mimsave('../../data/output/out.gif', images, fps=3)
