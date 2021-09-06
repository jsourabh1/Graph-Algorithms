from collections  import defaultdict

def dfs(node,visited):
	global graph
	visited.add(node)

	for i in graph[node]:

		if i not in visited:

			dfs(i,visited)

def is_connected():
	global vertex,graph
	visited=set()
	print(visited)

	dfs(0,visited)
	print(visited)
	if len(visited)==vertex:
		print("dfklajf")
		return True

	return False

def is_bridge(first,second):

	global graph

	index1=graph[first].index(second)
	index2=graph[second].index(first)

	del graph[first][index1]
	del graph[second][index2]

	return is_connected()


# Now printing all the bridges in teh graph




def addEdge(u,v):

	global graph
	graph[u].append(v)
	graph[v].append(u)

vertex=5
graph=defaultdict(list)
addEdge(1, 0)
addEdge(0, 2)
addEdge(2, 1)
addEdge(0, 3)
addEdge(3, 4)

is_bridges(1,2)
