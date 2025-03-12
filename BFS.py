#!/bin/python3
from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(set)
    
    def addNeighbour(self,node,neighbour):
        self.g[node].add(neighbour)
        self.g[neighbour].add(node)
    
    def bfs(self,node):
        dist = [0] * len(self.g)
        queue = list()
        visited = set()
        visited.add(node)
        queue.append(node)
        print(node)
        while len(queue) > 0:
            v = queue.pop(0)
            for w in self.g[v]:
                if w not in visited:   
                    print(w)
                    dist[w-1] = dist[v-1]+1
                    visited.add(w)
                    queue.append(w)  

        print(f"distance={dist}")




if __name__=="__main__":
    g = Graph()
    g.addNeighbour(1,2)
    g.addNeighbour(2,4)
    g.addNeighbour(3,4)
    g.addNeighbour(1,3)
    g.addNeighbour(4,5)
    g.bfs(3)
    #print(g.distance(1,5))
    


