
#dijkastra algorithm
import sys
from collections import defaultdict
class graph:

    def __init__(self,v):
        self.vrt=v



    def min_key(self,visited,dist):

        min=sys.maxsize

        for i in range(self.vrt):

            if i not in visited and dist[i]<min:
                min_index=i
                min=dist[i]
                # print(min_index)
        return min_index


    def main_body(self,source,graph):
        parent=[-1]*self.vrt

        visited=set()
        dist=[sys.maxsize]*self.vrt
        dist[source]=0
        for i in range(self.vrt):


          node=self.min_key(visited,dist)
          visited.add(node)

          for j in range(self.vrt):

            if graph[node][j]>0 and j not in visited and dist[j]>dist[node]+graph[node][j]:

              dist[j]=dist[node]+graph[node][j]
              parent[j]=node
        print(parent)

        print(dist)
g = graph(9)
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.main_body(0,graph)