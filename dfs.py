# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:37:14 2019

@author: Manas

This is a code for graph search by Depth First Search
"""
import networkx as nx

def DFS(G):
     # Mark all the vertices as not visited 
        visited = [False] * (G.number_of_nodes())
        distance = [0] * (G.number_of_nodes())
        for n in G.nodes():
           if visited[int(n)] == False:
               DFS_visit(n,G,visited,distance)
        print("start")
        return

def DFS_visit(u,G,visited,distance,time = 0):
    visited[int(u)] = True
    distance[int(u)] = time = time+1
    for v in G.neighbors(u):
        if visited[int(v)] == False:
            DFS_visit(v,G,visited,distance,time)
    
    distance[int(u)] = time = time+1
    print(u,'[',distance[int(u)],']',end="<-")
    return
            
    
G = nx.read_pajek('graph.paj')
DFS(G)