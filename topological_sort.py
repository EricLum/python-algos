# useful for dependencies

# the gist of the algo is to dfs a couple of times and then output leaf nodes to an order array.

# this order array may not be the same every time since ur node order can change depending on ur traversal + node selection.


# this only works on DAGs and it can't have any cycles so lets make a quick example with a depdency list

graph = {
    'A' : ['D'],
    'B' : ['D'],
    'C' : ['A', 'B'],
    'D' : ['H', 'G'],
    'E' : ['A', 'D', 'F'],
    'F' : ['K', 'J'],
    'G' : ['I'],
    'H' : ['I', 'J'],
    'I' : ['L'],
    'J' : ['M', 'L'],
    'K' : ['J'],
    'L' : [],
    'M' : []
}

class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph 
        self.visited = []
        self.output = []

    

    def solve(self):
        # start with a loop here to ensure we traversed each node
        for node in self.graph:

            if node not in self.visited:
                self.dfs(node)
        
        ##
        ##
        print(self.output)

    def dfs(self, node):
        # using each node, DFS it until we hit a termination point. then pop off these bad boys into the output.

        if len(graph[node]) == 0:
            # its a terminal node
            self.output.insert(0,node)
            self.visited.append(node)
            return

        # termination condition should be theres no neighbors && not visited.
        for neighbor in graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        
        # once u have ur neighbors/children visited, append urself.
        self.visited.append(node)
        self.output.insert(0,node)


topsort = TopologicalSort(graph)
topsort.solve()
