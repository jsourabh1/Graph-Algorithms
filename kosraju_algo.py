
from collections import defaultdict


#for strongly connected components 


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


    def Dfs_recfursive(self,node,visit,stack):

     	visit.add(node)
     	# print(visit)

     	for i in self.graph[node]:
     		# print(self.graph)
     		if i not in visit:
     			self.Dfs_recfursive(i,visit,stack)

     	stack=stack.append(node)




    def kosraju(self):

    	visit=set()
    	stack=[]
        
    	for i in list(self.graph):

    		if i not in visit:
    			self.Dfs_recfursive(i,visit,stack)
    		

    	obj=Graph()

    	for i in list(self.graph):
    		for j in self.graph[i]:
    			obj.addEdge(j,i)
    	
    	visit=set()
    	while stack:
    		ele=stack.pop()
    		ans=[]
    		
    		if ele not in visit:

    			obj.Dfs_recfursive(ele,visit,ans)

    			print(ans)





g = Graph()
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.kosraju()
