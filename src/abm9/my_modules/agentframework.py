# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:29:35 2023

@author: gy22fybm
"""

import random
import my_modules.geometry as gy


 #agent-environment interaction
class Agent: 
    
    def __init__(self, agents, i, environment, n_rows, n_cols, x = None, y = None):
       
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
        x : Integer
            For initialising the x coordinate of the agent.
        y : Integer
            For initialising the y coordinate of the agent.
        
        Returns
        -------
        None.
        
        """
        self.agents = agents
        self.i = i
        self.environment = environment
        if x == None:
            tnc = int(n_cols / 3)
            self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        else:
            self.x = x
        if y == None:
            tnr = int(n_rows / 3)
            self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        else:
            self.y = y
        self.store = random.randint(0, 99)
        self.store_shares = 0

        
    def __str__(self):
        return self.__class__.__name__ \
            + "(i=" + str(self.i) \
            + ", x=" + str(self.x) \
            + ", y=" + str(self.y) \
            + ", store=" + str(self.store) \
            + ", shares=" + str(self.store_shares) + ")"
            
    def __repr__(self):
        return str(self)
    
   
    def move(self, x_min, y_min, x_max, y_max):
            # Change agents[i] coordinates randomly
            # replace "agents[i]" with "self"
            # this code block makes the agents move diagonally
            
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
        #print ("Value of environment at locations before eating", self.environment[self.y][self.x])  
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
          
        #print ("Value of environment at locations after eating", self.environment[self.y][self.x])    

    def share(self, neighbourhood):
        # Create a list of agents in neighbourhood
        neighbours = []
        #print(self.agents[self.i])
        for a in self.agents:
            distance = gy.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
        # Calculate amount to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares
                    