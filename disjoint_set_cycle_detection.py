from collections import defaultdict
class solution :


	def __init__(self,vertex):

		self.vertex=vertex
		self.graf=defaultdict(list)

	def addEdge(self,u,v):

		self.graf[u].append(v)

	def find(self,i,parent):

		if parent[i]==-1:
			return i

		return self.find(parent[i],parent)

	def union(self,first,second,parent):

		parent[first]=second


	def cycle_detect(self):


		parent=[-1]*self.vertex

		for i in range(self.vertex):
			for j in self.graf[i]:
				first=self.find(i,parent)
				second=self.find(j,parent)

				if first==second:
					print("CYCLE")
					return 
				self.union(first, second,parent)

		print("NO CYCL")


g = solution(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)

g.cycle_detect()