#Test algorithme de Floyd-Warshall analyse et traitement amont/aval:
#GOYHEX Vincent: Université Paris8, BRGM.
#Données bidons.

import networkx as nx
import datetime
from osgeo import gdal
from osgeo import ogr


def main(path_nodes,path_edges,gid_nodes,gid_edges,weight_edges):
    #----------------------------------------------------------
    #NetworkX
    #----------------------------------------------------------
    #Import des données SHP à grapher:



    G=nx.Graph(name='Floyd_Warshall_script', date=str(datetime.datetime.now()))
    E = nx.read_shp(str(path_edges))
    N = nx.read_shp(str(path_nodes))

    G.add_nodes_from(N.nodes(data=True))
    G.add_edges_from(E.edges(data=True))

    #Changement de leur nom (pour l'instant, chaque valeur a le nom de ses coordonnées géographiques, c'est nul):
    #----------------------------------------------------------
    #D'abord pour les edges:

    x=0
    dict_edges={}
    total_edges=G.number_of_edges()
    print('Processing Edges')
    while x < total_edges:
        try: #En raison de la structure possible des fichiers, on place un try qui propose [1] ou [2], histoire de parer à toute éventualité.   
            dict_edges[G.edges(data=True)[x][0]]=G.edges(data=True)[x][2][str(gid_edges)]
            x=x+1
        except:
            dict_edges[G.edges(data=True)[x][0]]=G.edges(data=True)[x][1][str(gid_edges)]
            x=x+1
    #Maintenant pour les nodes:
            
    x=0
    dict_nodes={}
    count_nodes={}
    total_nodes=G.number_of_nodes()
    print('Processing Nodes')
    while x < total_nodes:
        try: #En raison de la structure possible des fichiers, on place un try qui propose [1] ou [2], histoire de parer à toute éventualité.
            dict_nodes[G.nodes(data=True)[x][0]]= G.nodes(data=True)[x][1][str(gid_nodes)]
            count_nodes[x]= G.nodes(data=True)[x][1][str(gid_nodes)]
            x=x+1
        except:
            dict_nodes[G.nodes(data=True)[x][0]]= G.nodes(data=True)[x][2][str(gid_nodes)]
            count_nodes[x]= G.nodes(data=True)[x][1][str(gid_nodes)]
            x=x+1
                       
    #On renomme les nodes/edges par leur id/gid originels:
    G=nx.relabel_nodes(G,dict_nodes)
    print('Processing Graph')
    #G=nx.relabel_edges(G,dict_edges) # Il semblerait que cette fonction n'existe pas... A rajouter manuellement, cela ne doit pas être bien dur.






    #----------------------------------------------------------
    #On lance maintenant le calcul d'itinéraire pour l'ensemble des paires de noeuds du réseau:
    starting_point=datetime.datetime.now()
    results = nx.floyd_warshall(G,weight=str(weight_edges))
    print(starting_point)
    print(datetime.datetime.now())
    print('Il aura fallu:  ' + str(datetime.datetime.now()-starting_point) + ' pour effectuer le calcul')

    text_file=open("Shitty_output.txt","w")
    text_file.write(str(results))
    text_file.close()
    

    open('Output.txt', 'w').close() #On efface Output.txt avant de lancer des opérations "append" dessus, histoire d'eviter d'avoir un mélange de résultats de plusieurs fichiers.
    with open('Output.txt', 'a') as text_file:
        
        
        gid=0
        i=0
        text_file.writelines('gid'+';'+'Origin'+';'+'Destination'+';'+'FloydWarshall_Cost'+'\n')
        while i<total_nodes:
                    
                origins=results[str(count_nodes[i])]
                i1=0
                for origin in origins:
                        while i1<total_nodes:
                                gid=gid+1
                                destinations=origins[str(count_nodes[i1])]
                                text_file.writelines( str(gid) + ';' + str(count_nodes[i] + ';' + str(count_nodes[i1]) + ';' + str(destinations) )+'\n')
                                i1=i1+1
                i=i+1
    text_file.close()
    print("Un fichier .TXT nommé \"Output\" a maintenant du apparaitre dans le dossier depuis lequel nous avons chargé le shapefile")

print("Pour lancer le programme, tapez \" main('path_nodes','path_edges','gid_nodes','gid_edges','weight_edges') \",")
print ("--"*30)
print("Remplacez \" Path \" par le chemin vers le fichier shapefile à transformer en graphe. !ATTENTION! Dans python les chemins '\\' ne sont pas reconnus, remplacer les '\\' par des'/'")
print("Indiquez le nom du champ GID de vos fichiers shapefile")
print ("Enfin, indiquez quelle variable vous allez vouloir utiliser comme poids pour faire tourner les calculs de distance")

print ("--"*30)
print("main('path_nodes','path_edges','gid_nodes','gid_edges','weight_edges')")
print ("--"*30)


