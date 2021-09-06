
from collections import defaultdict

class Graph:

    def __init__(self):

        self.graph=defaultdict(list)

    def addEdge(self,u,v):

        # this the un weighted graph 
        self.graph[u].append(v)
        # self.graph[v].append(u)


    def bfs(self,node):

        visit=[False]*(max(self.graph)+1)

        queue=[]

        queue.append(node)

        visit[node]=True


        while queue:

            node=queue.pop(0)
            print(node)

            for i in self.graph[node]:

                if not  visit[i]:
                    queue.append(i)
                    visit[i]=True

    def bfs_recursive(self,visit,queue):

        if not queue:
            return 

        node=queue.pop(0)
        visit[node]=True
        print(node)

        for i in self.graph[node]:

            if not visit[i]:
                queue.append(i)
               
        # print(queue)
        self.bfs_recursive(visit,queue)


INF=float("inf")
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

for i in range(len(graph)):

	for j in range(len(graph)):

		for k in range(len(graph)):

			graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])


print(graph)