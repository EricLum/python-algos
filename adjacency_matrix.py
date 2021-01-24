# a sample adjacency matrix

# A sample graph where undirected graph with two connected components.
# of ABC-DEF. Notice the 6x6 matrix has a 1 in each spot where there's 
# an edge between the two points.
graph = [
    [0,1,1,0,0,0],
    [1,0,1,0,0,0],
    [1,1,0,1,0,0],
    [0,0,1,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0]
]

# BFS Traversal in such a graph where the index is basically the node being traversed:
# {0:A, 1:B, 2:C, ...}
def BFS(graph):
    # create a queue to explore each child
    queue = [0]
    visited = []
    while len(queue) > 0:
        # mark node as visited

        index = queue.pop(0)
        print(index)
        if index in visited:
            continue
        visited.append(index)
        # print(index)
        #find neighbors
        for neighborIndex in range(len(graph)):
            # append 2 the queue if tehres a neighbor
            if graph[index][neighborIndex] == 1 and neighborIndex not in visited:
                queue.append(neighborIndex)
    
        
BFS(graph)


        
        