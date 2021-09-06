from collections import deque,defaultdict
import sys
def zero_one_BFS(src):
	global vertex,graph
	dist=[sys.maxsize]*vertex
	queue=deque()
	dist[src]=0
	queue.append(src)

	while queue:

		node=queue.popleft()

		for j,cost in graph[node]:

			if dist[j]>dist[node]+cost:
				# print(j)

				dist[j]=dist[node]+cost

				if cost==0:
					queue.appendleft(j)
				else:
					queue.append(j)


	print(dist)

def addEdge(u,v,cost):

	graph[u].append([v,cost])
	graph[v].append([u,cost])
graph=defaultdict(list)
vertex=9
addEdge(0, 1, 0)
addEdge(0, 7, 1)
addEdge(1, 7, 1)
addEdge(1, 2, 1)
addEdge(2, 3, 0)
addEdge(2, 5, 0)
addEdge(2, 8, 1)
addEdge(3, 4, 1)
addEdge(3, 5, 1)
addEdge(4, 5, 1)
addEdge(5, 6, 1)
addEdge(6, 7, 1)
addEdge(7, 8, 1)

# source node
src = 0
zero_one_BFS(src)




