



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
            	
                if  not  visit[i]:
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


    def Toplogical(self,node,visit,stack):

    	visit.add(node)

    	for i in self.graph[node]:

    		if i not in visit:
    			

    			self.Toplogical(i,visit,stack)

    	stack.append(node)

    	return 

    def Helper(self):
    	global vertex
    	visit=set()
    	stack=[]

    	for i in range(vertex):
    		


    		if i not in visit:

    			self.Toplogical(i, visit, stack)

    		


    	print(stack[::-1])


vertex=5
g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(3, 2)


g.Helper()