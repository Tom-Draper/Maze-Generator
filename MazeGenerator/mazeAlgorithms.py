import random

class MazeAlgorithms():
    
    def getOuterVetices(self, size):
        # Create lists of vertices at edge of maze
        topVertices = [x for x in range(size)]
        bottomVertices = [x for x in range(size*size - size, size*size)]
        leftVertices = [x * size for x in range(size)]
        rightVertices = [(x + 1) * size - 1 for x in range(size)]
        # Create one list of all vertices at edge of maze
        return topVertices + bottomVertices + leftVertices + rightVertices
    
    def getVertexEdge(self, vertex, size):
        topVertices = [x for x in range(size)]
        bottomVertices = [x for x in range(size*size - size, size*size)]
        leftVertices = [x * size for x in range(size)]
        rightVertices = [(x + 1) * size - 1 for x in range(size)]
        
        if vertex in topVertices:
            return 't'
        elif vertex in bottomVertices:
            return 'b'
        elif vertex in leftVertices:
            return 'l'
        elif vertex in rightVertices:
            return 'r'
        else:
            return 'm' # Middle of maze
    
    def primsAlgorithm(self, size, mazeTree, draw):
        visited = []
        frontiers = []
        
        starterVertices = self.getOuterVetices(size)
        # Choice first vertex from outer edge vertices
        firstVertex = random.choice(starterVertices) 
        
        visited.append(firstVertex)
        # Store adjacent vertices to first visited
        frontiers.append(mazeTree.tree.getConnections(firstVertex))
        
        # Draw the exit next to the first vertex
        draw.createExit(firstVertex, size, self.getVertexEdge(firstVertex, size))
        
        # Loop until all frontiers visited
        while frontiers:
            nextVertex = random.choice(frontiers)
            
            adjacent = mazeTree.tree.getConnections(nextVertex)
            
            # Find adjacent vertices that have been visited to join
            mergeWith = []
            for vertex in adjacent:
                if vertex in visited:
                    adjacent.remove(vertex)
                    mergeWith.add(vertex)
                    
            # Select vertex to merge with
            mergeVertex = random.choice(mergeWith)
                    
            visited.append(nextVertex)
            frontiers.append(adjacent)
            
            draw.removeEdge()