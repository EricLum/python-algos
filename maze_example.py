# take a typical RXC maze wehre S is the start and E is the end
# rocks are indicated by #
# the objective is to find the shortest path between S and E.
graph = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]

# can make a somewhat simple path trace by recreating ^ but empty

visited = [ ('Z', 'Z') for x in graph]

class MazeSolver:
    def __init__(self, graph):
        self.graph = graph
        self.rows =  len(graph)
        self.columns = len(graph[0])
        self.visited = [['' for _ in range(len(graph[0]))] for y in range(len(graph))]
        #direction vectors
        self.dx = [1, 0, 0, -1]
        self.dy = [0, -1, 1, 0]

        # queues for BFS with start point
        self.qx = [0]
        self.qy = [0]

    def solve(self):
        # overall idea is to add direction vectors until the right graph is chosen.

        # might be able to just destructively mark them

        while len(self.qx) > 0:

            currentX = self.qx.pop(0)
            currentY = self.qy.pop(0)
            
            currentNode = graph[currentY][currentX]


            if currentNode == 'E':
                print(currentY)
                print(currentX)
                return 'found'

            # mark as visited
            graph[currentY][currentX] = 'X'

            # get neighbors that will get traversed
            self.get_neighbors(currentX,currentY)


    def get_neighbors(self, x, y):

        for num in range(len(self.dx)):
            testX = self.dx[num]+x 
            testY = self.dy[num]+y

            if testX >= self.columns or testX < 0 or testY >=self.rows or testY < 0 :
                continue
            current = self.graph[testY][testX]
            if current == 'X' or current == '#':
                continue
            else:
                # add to queue
                self.qx.append(testX)
                self.qy.append(testY)
               
                # mark ancestor in visted for path reconstruction
                self.visited[testY][testX] = y,x
    
    def print_visited(self):
        print(self.visited)

    def reconstructPath(self, y, x):
        # given y and x and the visited array, keep printing out visiteds from y,x until you get to start or ''
        tempY = y 
        tempX = x
        while tempY != 'Z' and tempX != 'Z':
            a,b = self.visited[tempY][tempX]
            if (a == 'Z' and b == 'Z'):
                return
            tempY = a
            tempX = b
            print(tempY, tempX)
            # need 2 figure out how 2 add the last node
        

maze = MazeSolver(graph)
maze.solve()
# maze.print_visited()
maze.reconstructPath(4,3)
