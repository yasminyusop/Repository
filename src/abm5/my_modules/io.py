# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:08:39 2023

@author: gy22fybm
"""

import csv

'''
# Read input data (example when not as a function)
f = open('//ds.leeds.ac.uk/student/student13/gy22fybm/GEOG5990/Repository/data/input/in.txt', newline='')
data = []
for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
    row = []
    for value in line:
        row.append(value)
        #print(value)
    data.append(row)
f.close()
print(data)

'''

# Define function for to read input data
def read_data(filename):
    #open and sort data into lines and columns
    data = []
    f = open(filename, newline='')
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            #print(value)
        data.append(row)
        
 
    n_rows = len(data)
    
    # Test each row has the same length
    n_cols0 = len(data[0]) #first row used as reference
    for row in range(n_rows):
        n_cols = len(data[row])
        if n_cols != n_cols0: #code to check only if length is different
            print('Sad')
        
    return data, n_rows, n_cols #packs the results to the function definition
    
    f.close()
    
