# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:15:56 2023

@author: gy22fybm
"""


#While loop
x = 1
while (x < 10):
    print (x)
    x += 1
    
# Print the largest number less than 1 million that is divisible by 17
x = 1000000
while (x != 0):
    if (x % 17 == 0):
        break
    x -= 1
print(x)    #DONT KNOW WHAT IT MEANS

# Print odd numbers from 1 to 10
x = 0
while x < 10:
    x += 1
    if (x % 2) == 0:
        continue
    print(x, end =" ")
    
#For loop
for x in (0,1,2,3,4,5,6,7,8,9):
    print(x)

for x in range(10):  #for sequence of numbers
    print(x)    
    
names = ("Dale", "Albert", "Gordon", "Tamara", "Philip", "Chester", "Windom")
for name in names[1:5:2]:
    print(name) # <-- Prints "Albert", "Tamara". starts at position 1
                # until position 4 with a step of 2

names = ("Dale", "Albert", "Gordon", "Tamara", "Philip", "Chester", "Windom")
for i in range(len(names)):
    print(i, names[i])    
    
names = ("Dale", "Albert", "Gordon", "Tamara", "Philip", "Chester", "Windom")
for i in range(len(names)):
    print(i, names[i])
    i += 1
    print(i)    
    
names = ("Dale", "Albert", "Gordon", "Tamara", "Philip", "Chester", "Windom")
for i in range(2,len(names),2):
    print(names[i])    

for name in names[2::2]:
    print(name)    
    
names = ["Dale","Albert","Gordon","Tamara","Philip", "Chester","Windom"]
for name in names:
    names.remove(name)
print(names) 

names = ["Dale","Albert","Gordon","Tamara","Philip", "Chester","Windom"]
for name in names[:]:
    names.remove(name)
print(names)   

# Nesting loops
data = [
[0,1,2],
[3,4,5]
]
for row in data:
    for value in row:
        print(value, end=" ")
    print()
    
data = [
[0,1,2],
[3,4,5]
]
for row in range(len(data)):
    for col in range(len(data[row])):
        print(data[row][col], end=" ")
    print()    
    
#Moving window algorithm
data = [
[0,1,2,3,4,5],
[6,7,8,9,10,11],
[12,13,14,15,16,17],
[18,19,20,21,22,23],
[24,25,26,27,28,29],
[30,31,32,33,34,35]
]
result = []
for row in range(1, len(data) - 1):
    row_result = []
    for col in range(1, len(data[row]) - 1):
        value = data[row][col]
        for i in range(-1, 2):
            for j in range(-1, 2):
                value = max(value, data[row + i][col + j])
        row_result.append(value)
        print(value, end=" ")
    result.append(row_result)
    print()
#print(result)    