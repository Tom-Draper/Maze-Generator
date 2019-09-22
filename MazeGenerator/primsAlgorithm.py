# primsAlgorithm.py - holds a class that extends the mazeAlgorithm class and
# alters both the drawn maze that is displayed, and the graph properties to
# produce a randomly generated maze.

import random
from mazeAlgorithm import MazeAlgorithm

# Specific maze algorithm that uses the genral functions and structures from the 
# MazeAlgorithm class

# Prim's Algorithm
# Works as follows:
# Selects a starting cell (V1) on the edge of the maze, the outer maze wall 
# is now the exit to the maze.
# Cell v1 is the first to be visited and is added to the visited list.
# Each cell adjacent to this starting cell is added to a list of frontier cells.
# The next cell (V2) is selected from the frontier cells to merge.
# Chosen cell V2 is then merged with starting cell V1.
# Cell V2 has now been visited and added to the visited list and removed from
# frontiers.
# As cell V2 has now been visited, each adjacent cell to v2 (that has not 
# already been visited) is added to the frontiers list.
# The starting section of the algorithm is over.
# Another cell (VX) is chosen from the list of frontiers and merged with an already 
# visited cell next to it.
# If a chosen frontier cell has multiple adjacent cells that are visited, one
# is selected randomly.
# This is repeated until no more frontier cells exist and each cell has been
# visited.
class PrimsAlgorithm(MazeAlgorithm):
    
    def __init__(self, mazeGraph, draw):
        super().__init__(mazeGraph, draw)
    
    # Runs the algorithm on the maze graph
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
            
            self.visited.append(nextVertex) # Next vertex has now been visited
            self.frontiers.remove(nextVertex) # Remove so cannot be selected again
            
            # Erase line between maze cells and remove their connection
            self.draw.mergeCells(nextVertex, mergeVertex)
            self.mazeGraph.graph.removeConnection(nextVertex, mergeVertex)
            
            # Update algorithm progress bar
            updateBar = random.randint(0, self.mazeGraph.progressBar.updateFreq)
            if not self.mazeGraph.graph.displayDetail and updateBar == 0:
                maxVertexID = self.size * self.size
                self.mazeGraph.progressBar.displayAlgorithmProgress(len(self.visited) / maxVertexID)
        
        # Display complete progress bar
        self.mazeGraph.progressBar.displayAlgorithmProgress(100)