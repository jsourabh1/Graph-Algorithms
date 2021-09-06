#This is same as the DFS and BFS but there is small change is that we have to set the limit
def addEdge(u,v):

	global adj

	adj[u].append(v)

def DBS(src,dest,limit):
	global adj
	if src==dest:
		return True 
	if limit<=0:
		return False

	for i in adj[src]:

		if DBS(i,dest,limit-1):
			return True

	return False


def IDDS(src,dest,depth):

	for i in range(depth):

		if DBS(src,dest,i):
			print(True)
			return 
	print(False)

from collections import defaultdict
adj=defaultdict(list)
addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(1, 4)
addEdge(2, 5)
addEdge(2, 6)
  
target = 6; maxDepth = 3; src = 0

IDDS(src,target,maxDepth)
