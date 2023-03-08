# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:16:11 2023

@author: gy22fybm
"""

max_distance = 0
for a in agents:
    for b in agents:
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)
        
min_distance = distance = get_distance(agents[0][0], agents[0][1], agents[1][0], agents[1][1])
for i in range(len(agents)):
    a = agents[i]
    for j in range(i + 1, len(agents)):
            #if (j > i):
            print(i, j)
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            #print("distance between", a, b, distance)
            max_distance = min(max_distance, distance)
print("min_distance", max_distance)

    # Loop through and calculate distances
    max_distance = 0
    min_distance = get_distance(a[0], a[1], b[0], b[1])
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            min_distance = min(min_distance, distance)
            print("max_distance", max_distance /
                + "min_distance", min_distance)
            
    return max_distance, min_distance
        
        