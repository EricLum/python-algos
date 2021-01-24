# a sample adjacency matrix

# this is actually two different graphs lol. you'd have to look through whole thing  otherwise
# islands problem is just graph traversal with an extra loop to account for each row?

# A sample graph where undirected graph with two connected components.
# of ABC, DEF. Notice the 6x6 matrix has a 1 in each spot where there's 
# an edge between the two points.
#    A B C D E F 
# A    1 1 
# B
# C
# ... and so on
# graph = [
#     [0,1,1,0,0,0],
#     [1,0,1,0,0,0],
#     [1,1,0,0,0,0],
#     [0,0,0,0,1,1],
#     [0,0,0,1,0,1],
#     [0,0,0,1,1,0]
# ]

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




# BFS Traversal in such a graph
def BFS(graph):
    # create a queue to explore each child
    queue = [0]
    visited = []
    while len(queue) > 0:
        # mark node as visited
        print(queue)

        index = queue.pop(0)
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


        
        