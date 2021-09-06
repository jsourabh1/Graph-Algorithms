def find(parent,node):

	if parent[node]!=node:
		return find(parent,parent[node])
	return node

def union(parent,rank,x,y):

	if rank[x]>rank[y]:

		parent[y]=x

	elif rank[x]<rank[y]:
		parent[x]=y
	else:

		parent[x]=y
		rank[y]+=1

def addEdge(u,v,cost):
	global graf

	graf.append([u,v,cost])

def MST():
	global graf,vertex
	result=[]

	graf=sorted(graf,key=lambda x:x[2])

	parent=[]
	rank=[]

	for i in range(vertex):
		parent.append(i)
		rank.append(0) 

	index=0
	e=0
	print(graf)

	while e<vertex-1:
		first,second,cost=graf[index]
		index+=1
		x=find(parent,first)
		y=find(parent, second)

		if x!=y:

			e+=1
			result.append([first,second ,cost])
			union(parent, rank, x, y)
		print(index)
			

	print(result)








graf=[]
vertex=4
addEdge(0, 1, 10)
addEdge(0, 2, 6)
addEdge(0, 3, 5)
addEdge(1, 3, 15)
addEdge(2, 3, 4)
MST()

