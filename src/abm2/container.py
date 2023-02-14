# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:05:57 2023

@author: yasmi
"""

print('''This is \
all one line.
This is a second.''')

print("This is all " +
"one line.")
print("This is a second")

a = "A simple string to split."
deli = " " # What is used to split the String into parts
a_split0 = str.split(a, deli) # Doing the split one way
print(a_split0)
a_split1 = a.split(deli)
print(a_split1)

a = ()
print(len(a)) # Print the length of a
singleton = 'hello', # <-- Note the trailing comma.
print(len(singleton)) # Print the length of singleton
b = (1, "two", 4) # Pack 3 things into b
c, d, e = b # unpack b into three things (c will refer to 1, d to "two" and e to 4)
print(c)
print(d)

#try
f = ("fatih", 8, "m")
print ("f", f)
n, a, s = f
print(n)
print(a)
print(s)    

# Fibonacci series - the sum of the last two numbers in a sequence defines the next
a, b = 0, 1
print(a)
while b < 10:
    print(b)
    a, b = b, a+b
print(b)

# Ranges exercise. Unable to use as instructions. Used for, in command

for r in range(4):
    print(r)

for r in range(2,8,2): # generates 2,4,6
    print(r)
    
for r in range(0,-5,-1): # generates 0,-1,-2,-3,-4
    print(r)
    
for r in range(-10,15,5):
    print(r)    
    
a = tuple(range(5)) 
print(a)
type(a) #what is this for?

a = range(5) 
print(a)