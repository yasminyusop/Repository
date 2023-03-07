# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:29:35 2023

@author: gy22fybm
"""

import random

#class Agent():
   # pass


    
'''
#Initialiase in the corner  
    def __init__(self, i):
        
        The constructor method.
        
         Parameters
        ----------
        i : Integer
            To be unique to each instance.
        
         Returns
        -------
        None.
        
        
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass
   
'''

'''   
#initialise in the middle
    def __init__(self, i, n_rows, n_cols):
       
        
        The constructor method.
    
        Parameters
        ----------
        i : Integer
            To be unique to each instance.
        n_rows : Integer
            The number of rows in environment.
        n_cols : Integer
            The number of columns in environment.
        Returns
        -------
        None.
        
        
        self.i = i
        tnc = int(n_cols / 3)
        self.x = random.randint(0, tnc - 1) + tnc
        tnr = int(n_rows / 3)
        self.y = random.randint(0, tnr - 1) + tnr
 '''
 
 #agent-environment interaction
class Agent: 
    def __init__(self, i, environment, n_rows, n_cols):
   
        """
    The constructor method.
    
    Parameters
    ----------
    i : Integer
        To be unique to each instance.
    environment : List
        A reference to a shared environment
    n_rows : Integer
        The number of rows in environment.
    n_cols : Integer
        The number of columns in environment.
    
    Returns
    -------
    None.
    
        """
        self.i = i
        self.environment = environment
        self.x = random.randint(n_cols/3 - 1, 2 * n_cols / 3)
        self.y = random.randint(n_rows/3 - 1, 2 * n_rows / 3)
        self.store = 0



    #def __init__(self): <-initial codes used
        #self.x = random.randint(0, 99)
        #self.y = random.randint(0, 99)
        
    def __str__(self):
        return self.__class__.__name__ + "(x=" + str(self.x) \
            + ", y=" + str(self.y) + ")"   
            
    def __repr__(self):
        return str(self)
    
   
    def move(self, x_min, y_min, x_max, y_max):
            # Change agents[i] coordinates randomly
            # replace "agents[i]" with "self"
            # x-coordinate
            rn = random.random()
            #print("rn", rn)
            if rn < 0.5:
                self.x = self.x + 1
            else:
                self.x = self.x - 1
            # y-coordinate
            rn = random.random()
            #print("rn", rn)
            if rn < 0.5:
                self.y = self.y + 1
            else:
                self.y = self.y - 1
                
    def eat(self):
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10                