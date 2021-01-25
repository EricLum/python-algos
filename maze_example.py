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

class MazeSolver:
    def __init__(self, graph):
        self.graph = graph
        self.rows =  len(graph)
        self.columns = len(graph[0])
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
        
        

maze = MazeSolver(graph)
maze.solve()