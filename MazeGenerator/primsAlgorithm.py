import random
from mazeAlgorithm import MazeAlgorithm

class PrimsAlgorithm(MazeAlgorithm):
    
    def __init__(self, mazeGraph, draw):
        super().__init__(mazeGraph, draw)
    
    def run(self):
        if self.displayDetail:
            print('\nPrim\'s Algorithm on a ' + str(self.size) + ' x ' + str(self.size) + ' maze.\n')
            
        starterVertices = super().getOuterVertices()
        # Choice first vertex from outer edge vertices
        nextVertex = random.choice(starterVertices) 
        
        self.visited.append(nextVertex)
        # Store adjacent vertices to first visited
        self.frontiers += self.mazeGraph.graph.getConnections(nextVertex)
        
        # Draw the exit next to the first vertex
        self.draw.createExit(nextVertex, super().getVertexEdge(nextVertex))
        
        # Loop until all frontiers visited
        while self.frontiers:
            nextVertex = random.choice(self.frontiers)
            
            adjacent = self.mazeGraph.graph.getConnections(nextVertex)
            
            # Find adjacent vertices that have been visited to join
            mergeWith = []
            for vertex in adjacent:
                if vertex in self.visited:
                    # Potential vertex to merge with
                    mergeWith.append(vertex) 
                elif vertex not in self.frontiers:
                    # Add all new adjacent vertices to frontiers
                    self.frontiers.append(vertex) 
                    
            # Select vertex to merge with nextVertex
            mergeVertex = random.choice(mergeWith)
            
            self.visited.append(nextVertex)
            self.frontiers.remove(nextVertex)
            
            self.draw.mergeCells(nextVertex, mergeVertex)
            self.mazeGraph.graph.removeConnection(nextVertex, mergeVertex)
            
            # Update algorithm progress bar
            updateBar = random.randint(0, self.mazeGraph.progressBar.updateFreq)
            if not self.mazeGraph.graph.displayDetail and updateBar == 0:
                maxVertexID = self.size * self.size
                self.mazeGraph.progressBar.displayAlgorithmProgress(len(self.visited) / maxVertexID)
        
        self.mazeGraph.progressBar.displayAlgorithmProgress(100)