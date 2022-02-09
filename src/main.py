import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import dijkstra_path
import GeneticAlgorithmTraffic as ga
import random
import pickle
import csv

#Best Path
# source = 0
# destination = 9
# node = 10

def dijkstra(G, source, destination):
    shortest = nx.dijkstra_path(G, source, destination)
    length = nx.dijkstra_path_length(G, source, destination)
    return shortest, length
    
if __name__ == '__main__':
    #Generating Graph

    FILE = "/Volumes/GoogleDrive/マイドライブ/HI5/卒業研究/venv/SDA/data/Shimoshiromoto/"
    # FILE = "/Volumes/GoogleDrive/マイドライブ/HI5/卒業研究/venv/SDA/data/Sagara/"
    WHERE = "Shimoshiromoto_Hitoyoshi"
    # WHERE = "Sagara_Hitoyoshi"
    PATH = FILE + WHERE

    #get position of nodes
    with open(f'{PATH}_pos.pkl', 'rb') as f:
        pos = pickle.load(f)

    #view the list
    G = nx.read_edgelist(f"{PATH}.edgelist", data=(("weight", float),))
    # nx.draw(Gr, new_pos, node_size = 0.1)
    # plt.show()

    # get source and target
    with open(f'{FILE}osm.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        source , destination = str(int(l[0][0])), str(int(l[0][1]))
        
        
    
    # nx.draw_networkx(G, pos=pos)
    
    pathD, length =dijkstra(G, source, destination)
    print("Dijkstra", length)
    
   

    GA = ga.shortestPath(G, source, destination, pos)
    # GA.setSaveData()
    # GA.main()
    # print(GA.bestPath())
    GA.nodeColor("red", pathD)
    GA.edgeColor("red", pathD)
    GA.plotOnly(1, None)
    
    
    # GA.plot(1, None)
    

