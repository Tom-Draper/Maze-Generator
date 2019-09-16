from tree import Tree
import random

class MazeTree():
    
    def __init__(self, size, displayDetail, progressBar):
        self.size = size
        self.progressBar = progressBar
        self.tree = Tree(displayDetail)
        self.usedWeights = []
        
        self.createTree()
        self.initConnections()
        
    def createTree(self):
        maxVertexID = self.size * self.size
        # Create size squared vertices 
        for vertexID in range(maxVertexID):
            self.tree.addVertex(vertexID)
            
            # Update creating tree progress bar
            updateBar = random.randint(0, self.progressBar.updateFreq)
            if not self.tree.displayDetail and updateBar == 0:
                self.progressBar.displayCreateTreeProgress(vertexID / maxVertexID)
            
    def getVertexAbove(self, vertexID):
        # If vertex in top row
        if vertexID < self.size:
            return -1
        else:
            return vertexID - self.size
            
    def getVertexBelow(self, vertexID):
        # If vertex in bottom row
        if vertexID >= (self.size * (self.size - 1)):
            return -1
        else:
            return vertexID + self.size
        
    def getVertexLeft(self, vertexID):
        # If vertex in left column
        if (vertexID + self.size) % self.size == 0:
            return -1
        else:
            return vertexID - 1
        
    def getVertexRight(self, vertexID):
        # If vertex in left column
        if (vertexID + 1) % self.size == 0:
            return -1
        else:
            return vertexID + 1
            
    def initConnections(self):
        maxVertexID = self.size * self.size
        # Loop through each vertex in the maze
        for vertexID in range(maxVertexID):
            # Get the each adjacent vertex to current (if exists)
            left = self.getVertexLeft(vertexID)
            right = self.getVertexRight(vertexID)
            above = self.getVertexAbove(vertexID)
            below = self.getVertexBelow(vertexID)
            
            # If an adjacent vertex exists, and connection between two doesn't
                # already exist, create connection with random weight
            if left != -1 and not self.tree.connectionExist(vertexID, left):
                self.tree.addWeightedConnection(vertexID, left, self.getNewWeight())
            if right != -1 and not self.tree.connectionExist(vertexID, right):
                self.tree.addWeightedConnection(vertexID, right, self.getNewWeight())
            if above != -1 and not self.tree.connectionExist(vertexID, above):
                self.tree.addWeightedConnection(vertexID, above, self.getNewWeight())
            if below != -1 and not self.tree.connectionExist(vertexID, below):
                self.tree.addWeightedConnection(vertexID, below, self.getNewWeight())
            
            # Update adding weights progress bar
            updateBar = random.randint(0, self.progressBar.updateFreq)
            if not self.tree.displayDetail and updateBar == 0:
                self.progressBar.displayAddWeightsProgress(vertexID / maxVertexID)
                
    def getNewWeight(self):
        # Total number of connections needed squared to give plenty
        maxWeight = (((self.size-1) * self.size * 2) - 1) ** 2 
        
        # Get a unique weight
        weight = random.randint(0, maxWeight)
        while weight in self.usedWeights:
            weight = random.randint(0, maxWeight)
            
        self.usedWeights.append(weight)
        return weight
