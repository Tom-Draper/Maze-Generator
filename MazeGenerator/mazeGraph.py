from graph import Graph
import random

# Typical maze Graph:
# Vertex = digit, connection = | or -
# Size = 5
#  0 - 1 - 2 - 3 - 4
#  |   |   |   |   |
#  5 - 6 - 7 - 8 - 9
#  |   |   |   |   |
# 10 -11 -12 -13 -14
#  |   |   |   |   |
# 15 -16 -17 -18 -19
#  |   |   |   |   |
# 20 -21 -22 -23 -24

# Holds the functionality to create a new graph that is suitable for a maze
class MazeGraph():
    
    def __init__(self, size, displayDetail, progressBar):
        self.size = size
        self.progressBar = progressBar
        # Random number chosen in range, if matches progress bar updated
        self.updateBar = random.randint(0, self.progressBar.updateFreq)
        self.graph = Graph(displayDetail) # Create empty graph object
        self.usedWeights = []
        
        # Create graph and weightless grid-like connections
        self.createGraph()
        self.initConnections()
        
    # Add each vertex to the graph object
    def createGraph(self):
        maxVertexID = (self.size * self.size) - 1 # Largest vertex in square graph grid
        
        # Add each vertex to graph
        for vertexID in range(maxVertexID + 1):
            self.graph.addVertex(vertexID)
            
            # Update creating graph progress bar
            if not self.graph.displayDetail and self.updateBar == 0:
                self.progressBar.displayCreateGraphProgress(vertexID / maxVertexID)
            
    # Get the ID of the vertex above the input vertex in the grid graph
    def getVertexAbove(self, vertexID):
        # If vertex in top row of grid, no result.
        if vertexID < self.size:
            return -1
        else:
            return vertexID - self.size
            
    # Get the ID of the vertex below the input vertex in the grid graph
    def getVertexBelow(self, vertexID):
        # If vertex in bottom row of grid, no result.
        if vertexID >= (self.size * (self.size - 1)):
            return -1
        else:
            return vertexID + self.size
        
    # Get the ID of the vertex left of the input vertex in the grid graph
    def getVertexLeft(self, vertexID):
        # If vertex in left column of grid, no result
        if (vertexID + self.size) % self.size == 0:
            return -1
        else:
            return vertexID - 1
        
    # Get the ID of the vertex right of the input vertex in the grid graph
    def getVertexRight(self, vertexID):
        # If vertex in right column of grid, no result
        if (vertexID + 1) % self.size == 0:
            return -1
        else:
            return vertexID + 1
            
    # Create the initial grid-like connections between the graph vertices.
    # Each connection given a unique weight when created
    def initConnections(self):
        maxVertexID = self.size * self.size
        # Loop through each vertex in the maze
        for vertexID in range(maxVertexID):
            # Get the each adjacent vertex this vertex (if exists)
            left = self.getVertexLeft(vertexID)
            right = self.getVertexRight(vertexID)
            above = self.getVertexAbove(vertexID)
            below = self.getVertexBelow(vertexID)
            
            # If an adjacent vertex exists, and connection hasn't already been 
            # made, create connection with random weight
            if left != -1 and not self.graph.connectionExist(vertexID, left):
                self.graph.addWeightedConnection(vertexID, left, self.getNewWeight())
            if right != -1 and not self.graph.connectionExist(vertexID, right):
                self.graph.addWeightedConnection(vertexID, right, self.getNewWeight())
            if above != -1 and not self.graph.connectionExist(vertexID, above):
                self.graph.addWeightedConnection(vertexID, above, self.getNewWeight())
            if below != -1 and not self.graph.connectionExist(vertexID, below):
                self.graph.addWeightedConnection(vertexID, below, self.getNewWeight())
            
            # Update adding weights progress bar
            if not self.graph.displayDetail and self.updateBar == 0:
                self.progressBar.displayAddWeightsProgress(vertexID / maxVertexID)
              
    # Generate and return a new unique weight  
    def getNewWeight(self):
        # Total number of connections needed multipled by 100 to give plenty
        # of possible weights and result chance of recalculation
        maxWeight = (((self.size-1) * self.size * 2) - 1) * 100
        
        # Get a unique weight
        weight = random.randint(0, maxWeight)
        while weight in self.usedWeights:
            weight = random.randint(0, maxWeight)
            
        self.usedWeights.append(weight) # Add new weight to used weights
        return weight
