import networkx as nx
import matplotlib.pyplot as plt
import math
import pprint
import random
import copy

from networkx.classes.function import neighbors, nodes
from networkx.generators import intersection

PROBABILITY = 0.2
POPULATION = 10
GENERATION = 30

PATH = '/Volumes/GoogleDrive/マイドライブ/HI5/数理情報工学/GA応用/img/train/s5/'


class Gene:
    def __init__(self, i, s):
        self.index = i
        self.sequence = [s]
        self.fit = math.inf
        
        
    def __repr__(self):
        return self.__class__.__name__ + pprint.pformat(self.__dict__)  
    
class shortestPath:
    def __init__(self, G, source, destination, pos):
        """ Graph data"""
        self.G = G
        self.pos = pos
        self.source = source
        self.destination = destination

        """ Gene data"""
        # self.n_gene = len(G)-1
        self.population = POPULATION
        self.generation = GENERATION
        
        self.color_map = [ 'gray' for i in range( len(self.G) )]    
        for u,v in self.G.edges():
            self.G[u][v]["color"] = "gray"
        
        self.saveData = False
        

    def main(self):
        print("---- initial generation ----")
        self.setGene()
         
        # pprint.pprint(self.gene)
        
        for i in range(self.generation):
            print("---- generation of " + str(i+1)+ "----")
            self.first , self.second = copy.deepcopy(self.selection())
            
            self.crossover(self.first, self.second)
            if self.saveData:
                self.plot(1, None, self.first, i+1)
                self.plot(1, None, self.second, i+1)
            
            
            for i in range(self.population):
                self.fitness(i)
                
            self.result()
           
       
        
    def result(self):
        self.sorted = sorted(self.gene, key=lambda x: x.fit)
        # print(self.sorted[0].index,self.sorted[0].fit )
        # print(self.sorted[1].index,self.sorted[1].fit )
        
        # all
        for i in range(3):
            print(self.sorted[i].index,self.sorted[i].fit )
            

    def setSaveData(self):
        self.saveData = True    
        
                    
                
        
    def setGene(self):
        self.gene = []
        for i in range(self.population):
            self.gene.append( Gene(i, self.source) )
            self.gene[i].fit = self.fitness(i)
            
        for i in range(self.population):
            next = self.source
            while True:
                nodeList = list(self.G.neighbors(next))
                # if self.source in nodeList:
                #     nodeList.remove(self.source)
                next =  random.choice(nodeList)

                self.gene[i].sequence.append(next)
                # nodeList = list(self.G.neighbors(next))
                
                if next == self.destination:
                    break
            
            #brush up
            self.gene[i].sequence = self.norm( self.gene[i].sequence)

        
            self.fitness(i)     
            print( self.gene[i].index, self.gene[i].fit)
            
      
        if self.saveData:
            for i in range(self.population):
                print("plot")
                self.plot(1, None, self.gene[i], None)
            
            
        # pprint.pprint(self.gene)
                
                
        
        # for i in range(self.population):
            
    def fitness(self, number):
        fit = math.inf
        path =  self.gene[number].sequence
       
        if self.destination in path and nx.is_path(self.G, path):
            fit = self.getWeight(path)
            
        else:
            max = 10000000
            
            for i in range(len(path)-1):
                if nx.is_path(self.G, [path[i], path[i+1]]):
                    fit = max -self.getWeight([path[i], path[i+1]])

        self.gene[number].fit = fit
        

            
    def getWeight(self, path):
        weight = 0
        for i in range(len(path)-1):
            if nx.is_path(self.G, [path[i], path[i+1]]):
                weight += self.G[path[i]][path[i+1]]['weight']
            
        return weight
            
    
    def selection(self):
        # --- sort ---
        self.sorted = sorted(self.gene, key=lambda x: x.fit)
        """
        # best and worst ----
        target1 = self.sorted[0]
        target2 = self.sorted[-1]
        """
        
        """
        # random ----
        indexes = list(range(len(self.sorted)))
        
        parentIndex = random.choice(indexes)
        target1 = self.sorted[parentIndex]
        
        indexes.pop(indexes.index(parentIndex))
        
        parentIndex = random.choice(indexes)
        target2 = self.sorted[parentIndex]
        """
        
        
        # best and random -----

        target1 = self.sorted[0]
        
        indexes = list(range(1, len(self.sorted)))
        parentIndex = random.choice(indexes)
        target2 = self.sorted[parentIndex]
        
        

        return target1, target2
    
    def crossover(self, parent1, parent2):
        
        # --- save parent ---
        self.gene[0].sequence = parent1.sequence
        self.gene[1].sequence = parent2.sequence
        self.num = 2
        
        # --- make children ---
        # searching same points 
        intersection = self.intersection(parent1.sequence)
        
        shareNodes = []
        for node in intersection:
            if node in parent2.sequence:
                shareNodes.append(node)
            
        if self.source in shareNodes:
            shareNodes.pop(shareNodes.index(self.source))
        if self.destination in shareNodes:
            shareNodes.pop(shareNodes.index(self.destination))


        for i in range(len(shareNodes) -1 ):
            
            if random.random() < PROBABILITY:
                # print(">>", parent2.index, parent2.fit)
                childA, childB = self.pathSwap(parent1.sequence, parent2.sequence,shareNodes[i], shareNodes[i+1])
                
                # """
                if self.num < self.population :
                    self.gene[self.num].sequence = childA
                    self.num += 1
                
                if self.num < self.population :
                    self.gene[self.num].sequence = childB
                    self.num += 1
                # """

    
    def intersection(self, path):
        intersectionNode = []
        
        for node in path:
            neighbors = list(self.G.neighbors(node))
            if len(neighbors):
                intersectionNode.append(node)
                
        return intersectionNode
    
    def pathSwap(self, pathA, pathB, node1, node2):
        
        pathA1 = pathA[: pathA.index(node1)]
        pathA2 = pathA[pathA.index(node1) : pathA.index(node2)]
        pathA3 = pathA[pathA.index(node2) : ]
  
        pathB1 = pathB[: pathB.index(node1)]
        pathB2 = pathB[pathB.index(node1) : pathB.index(node2)]
        pathB3 = pathB[pathB.index(node2): ]
        
        new_pathA = self.norm(pathA1 + pathB2 + pathA3)
        new_pathB = self.norm(pathB1 + pathA2 + pathB3)
        
        # print(nx.is_path(self.G, new_pathA))
        # print(nx.is_path(self.G, new_pathB))
        

        
        return new_pathA, new_pathB
    
    def norm(self, path):
        for node in path:
            if path.count(node) > 1:
                start = path.index(node)
                path.pop(start)
                    
                while True:
                    if path[start] == node:
                        break
                    else :
                        path.pop(start)
                        
        return path
    
    def bestPath(self):
        self.sorted = sorted(self.gene, key=lambda x: x.fit)
        return self.sorted[0].sequence
    
    """
    def plot(self):
        path = self.bestPath()
        self.nodeColor("red", path)
        nx.draw(self.G, self.pos, node_size = 0.1,  node_color=self.color_map, label=None)
        plt.show()
    """
        
    def plot(self, node_size = None, with_labels=True, gene = None, generation = None):
        
        if gene is None:
            path = self.bestPath()
        else:
            path = gene.sequence
            self.color_map = [ 'gray' for i in range( len(self.G) )]    
            for u,v in self.G.edges():
                self.G[u][v]["color"] = "gray"
        
        self.nodeColor("blue", path)
        self.edgeColor('blue', path)
        self.nodeColor("red", [self.source])
        self.nodeColor("red", [self.destination])
        
        self.edge_color = [edge["color"] for edge in self.G.edges.values()]
        nx.draw(self.G, self.pos, node_size = node_size, node_color=self.color_map, with_labels=with_labels, edge_color=self.edge_color )
        
        if self.saveData:
            print("saving")
            if generation is None:
                generation = 'init'
            
            plt.savefig(PATH + str(generation) + '-' + str(gene.index) + '(' + str(gene.fit) + ').png')
            plt.close()
        else:
            plt.show()
        
    def plotOnly(self, node_size = None, with_labels=True):
        self.edge_color = [edge["color"] for edge in self.G.edges.values()]
        nx.draw(self.G, self.pos, node_size = node_size, node_color=self.color_map, with_labels=with_labels, edge_color=self.edge_color )
        plt.show()
        
    def nodeColor(self, color, nodes):
        graph = list(self.G.nodes())
        for n in self.G:
            if n in nodes:
                self.color_map[graph.index(n)] = color
                
    def edgeColor(self, color, edges):
        for i in range(len(edges)-1):
            self.G[edges[i]][edges[i+1]]["color"] = color
            
        
        
        