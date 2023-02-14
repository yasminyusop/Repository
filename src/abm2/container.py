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
    
a = (1,6,9,0,6)
print(min(a))
print(max(a))
print(a.index(6,0,4)) #print the first of item equal to 6 at or after index 0 and before index 4
print(a.count(6)) #print the count of items equal to 6 in a
b = (True, False)
print(any(b)) #print if any of the items in b are True   
    

#Lists list() exercise

a = [] # Create an empty list called a.
a.append("apple") # Append the String "apple" to the list a
print(len(a)) # Print the length of a
print(a[0]) # Print the first element of a
a.insert(0, 2) # Insert the Integer 2 into the first element of a
print(a)
a.reverse() # Reverse the order of elements in a
print(a)
del a[1] # Remove the element in a at index 1. USED DIFFERENT SYNTAX
print(a)
b = list((1, 2, 4, 8))
print(type(b))

#practise
print(b)
b.append(7)
print(b)
b.reverse()
print(b)


#Slices

#a[i:j] returns all the elements between i and j, including a[i] but not a[j]
#a[i:j:k] returns the same, but stepping k numbers each time.
#Slices must have at least [:] (slice everything), but the rest is optional.
#If j > len(a), the last position is used.
#If i is None or omitted, zero is used.
#If i > j, the slice is empty.
#What's important is the position of the colons.
#a[:2] # First two values.
#a[-2:] # Last two values.

a = [0,1,2,3,4]
b = [10,20,30]
a[1:3] = b # Note we replace 2 values with 3
print(b)
print(a)

a = [0,1,2,3,4]
b = [10,20]
a[1:5] = b # We replace 4 values with 2
print(a)

a = [1,2,3,4,5]
b = [10,20,30,40,50]
c = zip(a,b)
d = list(c) #need to do this step else result won't appear
print(d)

#Arrays exercise (array module)
import array
a = array.array('i',[0,0,0,0]) # Signed int type 'i'
a.insert(3, 21) # Insert in position 3 the value 21
print(a[3]) # Print the value at position 3

#Sets set() exercise
a = set() # Empty set
a.add("apple") # Add "apple" to a
a.add("orange") # Add "orange" to a
if "orange" in a:
    print('"orange" is in a')
print(a)    

#Dictionaries dict() exercise
nickname = {"thomas": "tom", "samuel": "sam", "samson": "sam"}
alias = dict([("rm", "remove"), ("cd", "change directory"), ("ls", "list")])
print(alias.get("rm")) # <-- This should print 'remove'.



