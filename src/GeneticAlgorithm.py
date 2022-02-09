import networkx as nx
import matplotlib.pyplot as plt
import math
import pprint
import random
from networkx.algorithms.centrality import second_order
from networkx.algorithms.cuts import node_expansion

from networkx.classes.function import neighbors, nodes


   
class Gene:
    def __init__(self, i, s):
        self.index = i
        self.sequence = [s]
        self.fit = math.inf
        
        
    def __repr__(self):
        return self.__class__.__name__ + pprint.pformat(self.__dict__)  
    
class shortestPath:
    def __init__(self, G, source, destination):
        """ Graph data"""
        self.G = G
        # self.pos = pos
        self.source = source
        self.destination = destination

        """ Gene data"""
        self.n_gene = len(G)-1
        self.population = 25
        self.generation = 3
        
        # self.main()
        
        """ verification """
        self.iter = 300
        
         
        
    
    def main(self):
        print("---- initial generation ----")
        self.setGene()
        
        for i in range(self.iter):
            print("---- generation of " + str(i+1)+ "----")
            self.first , self.second = self.selection()
            self.crossover(self.first, self.second)
            
            for i in range(self.population):
                self.fitness(i)
            
            self.first , self.second = self.selection()
            
            self.inheritance(self.first)
            self.gene[-1].sequence = self.mutation(self.gene[-1])
            self.fitness(self.gene[-1].index)
            
            # pprint.pprint(self.gene)
        
            self.result()
        # result
        
        # self.crossover()
        
    def result(self):
        self.sorted = sorted(self.gene, key=lambda x: x.fit)
        print(self.sorted[0].index,self.sorted[0].fit )
        print(self.sorted[1].index,self.sorted[1].fit )

                    
                    
                
        
    def setGene(self):
        self.gene = []
        for i in range(self.population):
            self.gene.append( Gene(i, self.source) )
            self.gene[i].fit = self.fitness(i)
            
        #random 
        """
        for i in range(self.population):
            nodeList = list(self.G.nodes)
            nodeList.remove(self.source)
            while(len(nodeList) > 0):
                node = random.choice(nodeList)
                self.gene[i].sequence.append(node)
                nodeList.remove(node)
                """

        for i in range(self.population):
            next = self.source
            while True:
                nodeList = list(self.G.neighbors(next))
                # if self.source in nodeList:
                #     nodeList.remove(self.source)
                next =  random.choice(nodeList)
                
                """
                if next in self.gene[i].sequence:   #if there are the node was already passed, restart
                    self.gene[i].sequence = [self.source]
                    next = self.source
                    continue
                """
                    
                self.gene[i].sequence.append(next)
                # nodeList = list(self.G.neighbors(next))
                
                if next == self.destination:
                    break
        
            self.fitness(i)     
            print( self.gene[i].index, self.gene[i].fit)
            
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
        
        target = self.sorted[1]
        
        nodes = target.sequence[1:len(self.sorted[0].sequence)-1]
        
        for s in self.sorted:
            if s.sequence != target.sequence:
                
                _second =  s
                break
        """
        for s in reversed(self.sorted):
            # are there same nodes ...? 
            if nodes[0] in s.sequence :
                # it can choose the sequence that diffetent of elite, not good one is chosen
                # so it will be more various
                if s.sequence != self.sorted[0].sequence:
                    second = s
                    break
        """
        return target, _second
    
    def crossover(self, parent1, parent2):
        
        # --- save parent ---
        self.gene[0].sequence = parent1.sequence
        self.gene[1].sequence = parent2.sequence
        self.num = 2
        
        # --- make children ---
        # nodes = self.sorted[0].sequence[1:len(self.sorted[0].sequence)-1]
        parent_nodes = parent1.sequence[1:len(parent1.sequence)-1]
        # print("nodes = ", parent1.index)
        
        
        
        p1_first = p1_last = []
        p2_first = p2_last = []
        
        # newSequence = []
        # if trying number is more than population, stop
        while True:
            for node in parent_nodes:
                if node in parent2.sequence :
                    # print("check", parent1.index)
                    p1_first = parent1.sequence[1:parent1.sequence.index(node)]
                    p1_last =  parent1.sequence[parent1.sequence.index(node)+1:len(parent1.sequence)-1]
                    
                    p2_first = parent2.sequence[1:parent2.sequence.index(node)]
                    p2_last =  parent2.sequence[parent2.sequence.index(node)+1:len(parent2.sequence)-1]
                    
                    shareNode = [node]
                    
                    # making 
                    children = [
                        [self.source] + p1_first + shareNode + p2_last + [self.destination], 
                        [self.source] + p2_first + shareNode + p1_last + [self.destination]
                    ]
                    
                    for i in range(len(children)):
                        if children[i] !=  parent1.sequence and children[i] !=  parent2.sequence:
                            # appending new diffrent sequence
                            if self.num <  self.population:
                                self.gene[self.num].sequence = children[i]
                                # print(self.num, children[i])
                                self.num += 1
                            else :
                                break
                
            break
    
    def inheritance(self, target):
        for i in range(self.num, self.population ):
            self.gene[i].sequence = target.sequence
            
        for i in range(self.population):
            self.fitness(i)
        
                              
    def mutation(self, target):
        base = target.sequence
        new = []
        
        for i in range(len(base)-1):
            new.append(base[i])
            nodes = self.betweenNode(base[i], base[i+1])
            # print('>>>' , nodes)
            print(nodes)
            if nodes:
                print("---")
                if random.random() < 0.1:
                    print("a")
                    between =  random.choice(nodes)
                    new.append(between)
             
        new.append(base[-1])
         
        return new
    
    def betweenNode(self, a, b):
        a_nodes = list(self.G.neighbors(a))
        print(a_nodes)
        b_nodes = list(self.G.neighbors(b))
        print(b_nodes)
        nodes = []
    
        for n in a_nodes:
            if n in b_nodes:
                nodes.append(n)
                
        return  nodes
    
    def intersection(self, path):
        for node in path:
            neighbors = list(self.G.neighbors(node))
            
            
        