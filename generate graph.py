# -*- coding: utf-8 -*-
"""
@author: Manas 
Spyder Editor

 This is a code for generation of graph
 for n number of nodes.
"""
import itertools
import random 
import networkx as nx
import matplotlib.pyplot as plt

def gen_graph(n):
    nodes = []
    # assiging nodes
    for i in range(n):
        nodes += [i]
    #making edges
    graph = []
    for i in range(int(n/4)):
        comb=[list(x) for x in itertools.combinations(nodes,2)]
        graph.extend(comb)
    
    n = int(len(graph))
    
    for i in range(1,int(n/2)):
        graph.remove(graph[random.randrange(int(n/2))])
    
    #Writing it in csv format
    file = open('graph.paj','w')
    
    file.writelines(["*Vertices ",str(len(nodes)),"\n"])
    for node in nodes:
       file.writelines([str(node)," ",'"',str(node),'"',"\n"])
    
    file.writelines(["*Edges","\n"])
    for edge in graph:
        file.writelines([" ".join([str(i) for i in edge]),"\n"])
    
    file.close()
    
    return graph

gen_graph(10)
G = nx.read_pajek('graph.paj')
print(nx.degree(G))
nx.draw(G)
plt.show()