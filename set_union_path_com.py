from collections import defaultdict
class graf:


	def __init__(self,vertex):

		self.vertex=vertex
		self.graph=defaultdict(list)

	def add_edge(self,u,v):

		self.graph[u].append(v)

class Subset:


	def __init__(self,parent,rank):

		self.parent=parent
		self.rank=rank

def find(subset,first):

	if subset[first].parent!=first:
		return find(subset,subset[first].parent)


	return subset[first].parent


def union(subset,first,second):

	if subset[first].rank>subset[second].rank:

		subset[second].parent=first

	elif subset[first].rank<subset[second].rank:

		subset[first].parent=second

	else:

		subset[first].parent=second
		subset[first].rank+=1



def cycle_detect(gra):

	subset=[]


	for i in range(gra.vertex):

		subset.append(Subset(i,0))


	for first in gra.graph:

		u=find(subset, first)

		for second in gra.graph[first]:

			v=find(subset, second)

			if u==v:
				print("CYCLE")
				break

			else:

				union(subset,u,v)

	for i in subset:

		print(i.parent,i.rank,i)

g = graf(4)
 
# add edge 0-1
g.add_edge(0, 1)
 
# add edge 1-2
g.add_edge(1, 2)
 
# add edge 0-2
g.add_edge(0, 3)

cycle_detect(g)