

# this search is diffrent from other search's becuase it uses priority queue
# which arrange all the edges according to the their weight

from queue import PriorityQueue
from collections import defaultdict

def addedge(u,v,cost):

	global adj

	adj[u].append((v,cost))
	adj[v].append((u,cost))

def IS(src,dest):
	global adj

	visit=set()

	visit.add(src)

	pq=PriorityQueue()
	# we have to keep the src weigth low so we can easily pop this 
	pq.put((0,src))

	while pq:

		node=pq.get()[1]

		print(node,end=" ")

		if node==dest:
			break


		for node,weight in adj[node]:

			if node not in visit:
				visit.add(node)

				pq.put((weight,node))


adj=defaultdict(list)

addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

src=0
dest=9
IS(src,dest)
