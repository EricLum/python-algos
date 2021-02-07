# Similar to SSSP, dijkstras is another single source path algorithm
# can't haven negative paths however.

import queue

graph = {
	"A": [("B", 4), ("C",1)],
	"B": [("D", 1)],
	"C": [("D", 5), ("B", 2)],
	"D": [("E", 3)],
	"E": []
}

class Dijkstras:
	def __init__(self, graph):
		self.graph = graph
		self.output = {}
		#initialize the dist array
		self.dist = {"A": float('inf'), "B": float('inf'), "C": float('inf'), "D":float('inf'), "E": float('inf')}
		self.q = queue.PriorityQueue()

		self.visited = {"A": False, "B": False, "C": False, "D":False, "E": False}

	def solve(self):

		self.q.put((0, "A"))
		self.dist["A"] = 0

		while self.q.qsize() > 0:
			# take out from queue
			currentLength,currentName = self.q.get()
			
			self.visited[currentName] = True

			# add to queue
			for neighbor in self.graph[currentName]:

				name,length = neighbor 
				print(length,name)
				if self.visited[name] == True:
					continue


				#relaxation
				newDist = length + self.dist[currentName]
				if newDist < self.dist[name]:
					self.dist[name] = newDist
					self.q.put((newDist,name))



		print(self.dist)
	
test = Dijkstras(graph)
test.solve()