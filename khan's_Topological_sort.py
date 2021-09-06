



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


    def Khan_algo(self,N):


    	in_degree=[0]*(N)

    	for i in range(N):

    		for j in self.graph[i]:

    			in_degree[j]+=1

    	
    	ans=[]

    	count=0
    	queue=[]
    	for i in range(N):
    		if in_degree[i]==0:
    			queue.append(i)

    	while queue:

    		node=queue.pop(0)

    		ans.append(node)

    		for i in self.graph[node]:
    			in_degree[i]-=1
    			if in_degree[i]==0:
    				queue.append(i)

    		

    		count+=1
    	print(ans)

    	if count!=N:
    		print("There is a cycle ")
    		return 
    	






# we detect the cycle in the directed graph

g = Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.Khan_algo(3)

#       # 5---->2---->3--->1<---4
#       # |                     |
#       # 0<---------------------


