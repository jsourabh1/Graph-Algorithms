  


def addEdge(u,v,cost):

	global adj

	adj.append([u,v,cost])

def Bellman_ford(src):

	global adj,vertex

	#source intialization 
	dist=[float("inf")]*vertex
	dist[src]=0
	for _ in range(vertex-1):

		for u,v,cost in adj:

			if dist[u]!=float("inf") and dist[u]+cost<dist[v]:

				dist[v]=dist[u]+cost

	for u,v,cost in adj:

		if dist[u]!=float("inf") and dist[u]+cost<dist[v]:
			print("There is an negative cycle")
			return 

	print(dist)


adj=[]
vertex=5
addEdge(0, 1, -1)
addEdge(0, 2, 4)
addEdge(1, 2, 3)
addEdge(1, 3, 2)
addEdge(1, 4, 2)
addEdge(3, 2, 5)
addEdge(3, 1, 1)
addEdge(4, 3, -3)

Bellman_ford(0)

	
