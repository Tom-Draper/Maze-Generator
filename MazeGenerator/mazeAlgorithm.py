import random

class MazeAlgorithm():
    
    def __init__(self, mazeTree, draw):
        self.size = mazeTree.size
        self.displayDetail = mazeTree.tree.displayDetail
        self.mazeTree = mazeTree
        self.draw = draw
        
        self.visited = []
        self.frontiers = []
            
    def getTopVertices(self):
        return [x for x in range(self.size)]
    
    def getBottomVertices(self):
        return [x for x in range((self.size * self.size) - self.size, self.size*self.size)]
    
    def getLeftVertices(self):
        return [x * self.size for x in range(self.size)]
    
    def getRightVertices(self):
        return [(x + 1) * self.size - 1 for x in range(self.size)]
        
    def getOuterVertices(self):
        # Create lists of vertices at edge of maze
        topVertices = self.getTopVertices()
        bottomVertices = self.getBottomVertices()
        leftVertices = self.getLeftVertices()
        rightVertices = self.getRightVertices()
        # Create one list of all vertices at edge of maze
        return topVertices + bottomVertices + leftVertices + rightVertices
    
    def getVertexEdge(self, vertex):
        # Create lists of vertices at edge of maze
        topVertices = self.getTopVertices()
        bottomVertices = self.getBottomVertices()
        leftVertices = self.getLeftVertices()
        rightVertices = self.getRightVertices()
        
        # If in the corners, randomly choose between two edges
        if vertex in topVertices and vertex in leftVertices:
            choice = random.randint(0, 2)
            if choice == 0:
                return 't'
            else:
                return 'l'
        elif vertex in topVertices and vertex in rightVertices:
            choice = random.randint(0, 2)
            if choice == 0:
                return 't'
            else:
                return 'r'
        elif vertex in bottomVertices and vertex in leftVertices:
            choice = random.randint(0, 2)
            if choice == 0:
                return 'b'
            else:
                return 'l'
        elif vertex in bottomVertices and vertex in rightVertices:
            choice = random.randint(0, 2)
            if choice == 0:
                return 'b'
            else:
                return 'r'
        # Get edge vertex is on
        elif vertex in topVertices:
            return 't'
        elif vertex in bottomVertices:
            return 'b'
        elif vertex in leftVertices:
            return 'l'
        elif vertex in rightVertices:
            return 'r'
        else:
            return 'm' # Middle of maze 