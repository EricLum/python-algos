# recall taht you basically can find connected components in an unweighted graph by doing DFS on each node on the graph.

#an example graph
g = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['B', 'A'],
    'D': ['E', 'F'], 
    'E': ['D', 'F'],
    'F': ['E', 'D']
}

visited = {}

colors = ['red', 'blue', 'yellow', 'green', 'indigo', 'violet']
colorCounter = 0


# additional thing you can do is pass a color on each traversal. this way you can label your components into distinct groups
def start():
    global colorCounter
    for node in g:
        if node in visited:
            # do nothing
            continue
        else:
            traverse(node)
            colorCounter+=1

    print(visited)



def traverse(node):
    # mark as visited
    global colorCounter
    visited[node] = colors[colorCounter]
    print(node)

    # traverse
    neighbors = g[node]
    for neighbor in neighbors:
        if neighbor in visited:
            continue
        else:
            traverse(neighbor)


start()