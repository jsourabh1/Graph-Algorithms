
'''
Time Complexity of the above program is O(V^2). 
If the input graph is represented using adjacency list, 
then the time complexity of Prim’s algorithm can be reduced 
to O((E+V) log V) with the help of binary heap

'''

import sys
from collections import defaultdict

class solution :

	def minkey(self,key,mset):
		global vertex
		minn=sys.maxsize
		

		for i in range(vertex):

			if key[i]<minn and mset[i]==False:
				minn=key[i]
				index=i

		return index



	def PrismMST(self):
		global vertex,graph
		key=[sys.maxsize]*vertex

		parent=[0]*vertex

		key[0]=0

		mset=[False]*vertex

		parent[0]=-1

		for i in range(vertex):


			index=self.minkey(key,mset)
			print(index)
			# print(index)

			mset[index]=True

			for i in range(vertex):

				if mset[i]==False and graph[index][i]>0 and key[i]>graph[index][i]:

					key[i]=graph[index][i]
					parent[i]=index
		print(parent)
		# for i in range(1,vertex):
		# 	print(graph[i][parent[i]])

g = solution()
graph = [ [ 0, 2, 0, 6, 0 ],
              [ 2, 0, 3, 8, 5 ],
              [ 0, 3, 0, 0, 7 ],
              [ 6, 8, 0, 0, 9 ],
              [ 0, 5, 7, 9, 0 ], ]
vertex=5

g.PrismMST()