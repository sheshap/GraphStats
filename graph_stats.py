"""
Code Developed as part of Warmup Project for the Course, Spring 2017
Course Name: CIS 700 The Strucutre of Complex Networks
Instructor: Dr. Sucheta Soundarajan

Developed by: Shivanand Venkanna Sheshappanavar
Script name: graph_stats.py
Command to run: python graph_stats.py <filename>.txt
Description: Script works only for undirected graphs with datasets containing two columns
of fromNodeID to toNodeID. No edge weights or labels are supported at this stage(Feb 15th 2017)
"""

import sys
import networkx as nx
import matplotlib.pyplot as plt

filename = sys.argv[1]
g=nx.read_edgelist(filename,create_using=nx.Graph(),nodetype=int)

print nx.info(g)
plt.figure()
sp=nx.spring_layout(g)
plt.axis('off')
nx.draw_networkx(g,pos=sp,with_labels=False, node_size=35)

#diameter of largest connected component
gcc=sorted(nx.connected_component_subgraphs(g),key=len,reverse=True)
title="diameter of largest connected component = "+str(nx.diameter(gcc[0]))

#number of connected components
newtitle=title + '\n number of connected components = ' +str(nx.number_connected_components(g))

plt.title(newtitle)
plt.savefig("1.png")

#degree distribution
degrees = nx.degree(g)
print degrees
degree_values=sorted(nx.degree(g).values(),reverse=False)
degree_dist=[degrees.values().count(x) for x in degree_values]
plt.figure()
plt.plot(degree_values,degree_dist,'r+')
plt.title("Degree Distribution")
plt.xlabel('Degree')
plt.ylabel('Number of Nodes')
plt.savefig("2.png")

#power law
plt.figure()
plt.loglog(degree_values, degree_dist, basex=2)
plt.grid(True)
plt.title('loglog base 2 on x')

P = degrees.keys()
Q = degrees.values()

lowdeg = min(Q)
highdeg = max(Q)

#clustering coefficient vs degree
clustering = nx.clustering(g)
X = clustering.keys()
Y = clustering.values()

new_dic = dict()
for i in range(lowdeg,highdeg+1):
    count = 0
    sum = 0
    for j in P:
        if degrees[j] == i:
            count = count + 1
            sum = sum + clustering[j]
    if count != 0:
        new_dic[i] = sum/count
    else:
        new_dic[i] = 0

A = new_dic.keys()
B = new_dic.values()

plt.figure()
plt.plot(A,B,'b*')
plt.xlabel('Degree')
plt.ylabel('Mean Clustering co-efficient')
title="Mean Clustering co-efficient of Graph = "+str(nx.average_clustering(g))
plt.title(title)
plt.savefig("3.png")

plt.figure()
plt.plot(X,Y,'gx')
plt.title("Clustering Co-efficients")
plt.xlabel('NodeID')
plt.ylabel('Clustering Co-efficient')

plt.show()
plt.savefig("4.png")
plt.close()
