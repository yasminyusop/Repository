# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:15:26 2023

@author: gy22fybm
"""
import math

# Define get_distance to
# calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4

def get_distance(x0,y0,x1,y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

