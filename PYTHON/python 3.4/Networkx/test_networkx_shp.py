# -*- coding: utf-8 -*-
import networkx as nx
from osgeo import gdal
from osgeo import ogr
import datetime
#Clear system function (we dont want it to use too much memory if we repeatedly ask for screenplay
import os
clear = lambda:os.system('cls')
clear()


#--------------------------------------------------
#GDAL
#--------------------------------------------------
driver = ogr.GetDriverByName("ESRI SHAPEFILE")
datasource = driver.Open("D:/Documents/goyhex/Travail/Python_programs/python_data/network_completed_centroid1.shp")
datasource1 = driver.Open("D:/Documents/goyhex/Travail/Python_programs/python_data/network_completed_centroid_vertices.shp")
edges = datasource.GetLayer()
nodes = datasource1.GetLayer()
print( nodes.GetName())
print (edges.GetName())
print (nodes.GetExtent()) # same extent for the two of them, good.
print (edges.GetExtent()) #same extent for the two of them, good.
print (nodes.GetFeatureCount())
print (edges.GetFeatureCount())


#Check the column names for edges and nodes
nodesDef=nodes.GetLayerDefn()
edgesDef=edges.GetLayerDefn()
i=0
while i<5:
    #print(nodesDef.GetFieldDefn(i).GetName()+("     -- node"))
    print(edgesDef.GetFieldDefn(i).GetName())
    i=i+1

print('#'*30)

for i in range(10):
    print (edges.GetFeature(i).GetFieldAsString("class_adm"))



#--------------------------------------------------
#NETWORKX
#--------------------------------------------------
print('#'*30+'So far so good...'+'#'*30)

G = nx.Graph(name='Agregator',date='07/04/2015',Author='Goyhex Vincent')
print(G.number_of_edges()) #empty
print(G.number_of_nodes()) #empty
#Let the data flow into those empty vessels.
E = nx.read_shp('D:/Documents/goyhex/Travail/Python_programs/python_data/network_completed_centroid1.shp')
N = nx.read_shp('D:/Documents/goyhex/Travail/Python_programs/python_data/network_completed_centroid_vertices.shp')

G.add_nodes_from(N.nodes(data=True))
G.add_edges_from(E.edges(data=True))

print(G.number_of_edges()) #working
print(G.number_of_nodes()) #working
print(nx.info(G))
print(nx.density(G))
print(nx.is_directed(G))




#WARSHALL_first_try:
#Les print et starting_point sont là pour savoir combien de temps le calcul a pris.

starting_point=datetime.datetime.now()
print('#'*30+' Here we go... ' + '#'*30)
#results = nx.floyd_warshall(G,weight='longueur')
print(datetime.datetime.now())               
print(starting_point)
print(datetime.datetime.now()-starting_point)

#securités:  
text_file = open("Output.txt", "w")
text_file.write(str(results))
text_file.close()
text_file = open("Output1.txt", "w")
print('Your files are ready my good sir.')
text_file.write(results)
text_file.close()

