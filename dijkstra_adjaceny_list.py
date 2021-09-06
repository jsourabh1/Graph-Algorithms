#dijkastra algorithm
import sys
from heapq import *
from collections import defaultdict
class graph:

    def __init__(self,v):
        self.vrt=v

        self.graph=defaultdict(list)

    def main_body(self,source):

        # visited=set()
        dist=[sys.maxsize]*self.vrt
        dist[source]=0

        heap=[]
        heapify(heap)

        heappush(heap,(0,source))

        print(self.graph)

        while heap :


          weigth,node=heappop(heap)
          # visited.add(node)

          for j,cost in self.graph[node]:

            if dist[j]>dist[node]+cost:

              dist[j]=dist[node]+cost
              print(dist)

              heappush(heap,(dist[j],j))
        print(dist)

        

    def addEdge(self,u,v,cost):

      self.graph[u].append((v,cost))
      # self.graph[v].append((u,cost))


graph = graph(9)
graph.addEdge(1,2, 1)
graph.addEdge(2,3, 2)
graph.addEdge(3, 4, 3)
graph.addEdge(4, 1, 2)
graph.addEdge(2, 5, -3)
graph.addEdge(3, 8, -5)
graph.addEdge(4, 7, 2)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 3)
graph.addEdge(7, 8, 2)
graph.addEdge(8, 6, 1)
graph.addEdge(7, 5, 1)

graph.main_body(0)
