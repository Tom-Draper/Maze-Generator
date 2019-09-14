from tree import Tree
import random

class MazeTree():
    
    def __init__(self, size):
        self.tree = Tree()
        self.usedWeights = []
        
        self.createTree(size)
        self.initConnections(size)
        
    def createTree(self, size):
        # Create size squared vertices 
        for vertexID in range(size * size):
            self.tree.addVertex(vertexID)
            
    def getVertexAbove(self, size, vertexID):
        # If vertex in top row
        if vertexID < size:
            return -1
        else:
            return vertexID - size
            
    def getVertexBelow(self, size, vertexID):
        # If vertex in bottom row
        if vertexID >= (size * (size - 1)):
            return -1
        else:
            return vertexID + size
        
    def getVertexLeft(self, size, vertexID):
        # If vertex in left column
        if (vertexID + size) % size == 0:
            return -1
        else:
            return vertexID - 1
        
    def getVertexRight(self, size, vertexID):
        # If vertex in left column
        if (vertexID + 1) % size == 0:
            return -1
        else:
            return vertexID + 1
            
    def initConnections(self, size):
        # Loop through each vertex in the maze
        for vertexID in range(size*size):
            # Get the each adjacent vertex to current (if exists)
            left = self.getVertexLeft(size, vertexID)
            right = self.getVertexRight(size, vertexID)
            above = self.getVertexAbove(size, vertexID)
            below = self.getVertexBelow(size, vertexID)
            
            # If an adjacent vertex exists, and connection between two doesn't
                # already exist, create connection with random weight
            if left != -1 and not self.tree.connectionExist(vertexID, left):
                self.tree.addWeightedConnection(vertexID, left, self.getNewWeight(size))
            if right != -1 and not self.tree.connectionExist(vertexID, right):
                self.tree.addWeightedConnection(vertexID, right, self.getNewWeight(size))
            if above != -1 and not self.tree.connectionExist(vertexID, above):
                self.tree.addWeightedConnection(vertexID, above, self.getNewWeight(size))
            if below != -1 and not self.tree.connectionExist(vertexID, below):
                self.tree.addWeightedConnection(vertexID, below, self.getNewWeight(size))
            
                
    def getNewWeight(self, size):
        maxWeight = ((size-1) * size * 2) - 1 # Total number of connections
        
        # Get a unique weight
        weight = random.randint(0, maxWeight)
        while weight in self.usedWeights:
            weight = random.randint(0, maxWeight)
            
        self.usedWeights.append(weight)
        return weight