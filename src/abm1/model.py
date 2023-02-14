# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:23:48 2023

@author: yasmi
"""
import random

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)

if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Initialise variable x1
x1 = 0
print("x1", x1)

# Initialise variable y1
y1 = 0
print("y1", y1)

# Change x1 and y1 randomly
rn = random.random()
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1", x1)

if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1", y1)

# Change coordinate initialisation
# use randint() 

# Set the pseudo-random seed for reproducibility
# random.seed(0) IS THIS NEEDED?

# Re-initialise variable x0
a = random.randint(0,99)
x0 = a

print("x0", x0)

# Re -initialise variable y0
b = random.randint(0,99)
y0 = b
print("y0", y0)

# QUESTION: why renders same value? 

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# First, initialise (x0,y0)
x0 = 0
y0 = 0

print("(x0,y0)", x0, y0)

# Then, initialise (x1,y1)
x1 = 3
y1 = 4

print("(x1,y1)", x1, y1)


# Calculate the difference in the x coordinates.
dx = x1 - x0

print ("dx", dx)

# Calculate the difference in the y coordinates.
dy = y1 - y0

print ("dy", dy)

# Square the differences 
dx2 = dx ** 2
dy2 = dy ** 2

print ("dx2,dy2)", dx2, dy2)

# and add the squares
z2 = dx2 + dy2

print ("z2" , z2)

# Calculate the square root
z = z2 ** 0.5

print ("z", z)

