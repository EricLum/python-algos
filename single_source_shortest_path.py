# Single source shortest path is basically a bunch of BFS that updates a globalish type of length store that has the shortest length to each node given a starting source node. It only works on DAGs

#example 
graph = {
    'A': [('B',3), ('C',6)],
    'B': [('C',4), ('D',4), ('E', 11)],
    'C': [('D', 8), ('G', 11)],
    'D': [('E', -4), ('F', 5), ('G', 2)],
    'E': [('H', 9)],
    'F': [('H', 1)],
    'G': [('H', 2)],
    'H': []
}

# So we can create a simple class to hold access to some global values as we do SSSP

class SSSP:
    def __init__(self, graph):
        self.graph = graph
        self.output = {'A': 0, 'B': float('inf'),'C': float('inf'),'D': float('inf'),'E': float('inf'),'F': float('inf'),'G': float('inf'), 'H': float('inf')}
        self.visited = []
    
    def solve(self):
        # we know to start with A since its the single source.
        queue = ['A']

        while len(queue) > 0:
            #visit the edges outwards + create values in output for the shortest path so far.
            current = queue.pop()
            for edge in graph[current]:
                destination, length = edge
                if not destination in self.visited:
                    queue.append(destination)
                    if self.output[current] + length < self.output[destination]:
                        # update path length to destination
                        self.output[destination] = self.output[current] + length
    
        return self.output


mygraph =  SSSP(graph)
print(mygraph.solve())