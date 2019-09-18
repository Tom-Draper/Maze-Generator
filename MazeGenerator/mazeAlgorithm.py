import random

# Holds the general functionality and structures used by a maze algorithm
# Parent class of specific maze algorithm classes
class MazeAlgorithm():
    
    def __init__(self, mazeGraph, draw):
        self.size = mazeGraph.size
        self.displayDetail = mazeGraph.graph.displayDetail
        self.mazeGraph = mazeGraph
        self.draw = draw
        
        self.visited = []
        self.frontiers = []
            
    # Return vertices along the top row of the maze graph
    def getTopVertices(self):
        return [x for x in range(self.size)]
    
    # Return vertices along the bottom row of the maze graph
    def getBottomVertices(self):
        return [x for x in range((self.size * self.size) - self.size, self.size*self.size)]
    
    # Return vertices along the far left column of the maze graph
    def getLeftVertices(self):
        return [x * self.size for x in range(self.size)]
    
    # Return vertices along the far right column of the maze graph
    def getRightVertices(self):
        return [(x + 1) * self.size - 1 for x in range(self.size)]
        
    # Return vertices along the outer edges of the maze graph
    def getOuterVertices(self):
        # Create lists of vertices at edge of maze
        topVertices = self.getTopVertices()
        bottomVertices = self.getBottomVertices()
        leftVertices = self.getLeftVertices()
        rightVertices = self.getRightVertices()
        # Create one list of all vertices at edge of maze
        return topVertices + bottomVertices + leftVertices + rightVertices
    
    # Get and return the outer maze edge a particular vertex lies in the form 
    # of a character
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