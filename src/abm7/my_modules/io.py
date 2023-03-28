# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:08:39 2023

@author: gy22fybm
"""

import csv


#define function for read_data

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
 
    
def write_data(filename,data):
    # Open a file for writing
    f = open(filename, 'w', newline='')
    # Write a to the file
    writer = csv.writer(f, delimiter=' ')
    for row in data:
        writer.writerow(row) # List of values.
    # Close the file
    f.close() 


    
'''
filename = '//ds.leeds.ac.uk/student/student13/gy22fybm/GEOG5990/Repository/data/input/in.txt'
data, n_rows, n_cols = read_data(filename) #unpacks operations done in function definition, hence whatever print will appear
#print(data)
print(n_rows)
print(n_cols)
'''