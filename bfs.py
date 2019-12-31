# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:49:27 2019

@author: Manas
This is a code for graph search by Breath First Search
"""
import networkx as nx

def BFS(G, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (G.number_of_nodes()) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in G.neighbors(str(s)): 
                if visited[int(i)] == False: 
                    queue.append(int(i)) 
                    visited[int(i)] = True
        return 

G = nx.read_pajek('graph.paj')
BFS(G, 0)