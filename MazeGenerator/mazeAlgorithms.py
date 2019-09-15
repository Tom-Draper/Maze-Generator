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
    
    def primsAlgorithm(self, size, mazeTree, draw):
        visited = []
        frontiers = []
        
        starterVertices = self.getOuterVetices(size)
        # Choice first vertex from outer edge vertices
        nextVertex = random.choice(starterVertices) 
        
        visited.append(nextVertex)
        # Store adjacent vertices to first visited
        frontiers += mazeTree.tree.getConnections(nextVertex)
        
        # Draw the exit next to the first vertex
        draw.createExit(nextVertex, size, self.getVertexEdge(nextVertex, size))
        
        # Loop until all frontiers visited
        while frontiers:
            nextVertex = random.choice(frontiers)
            
            adjacent = mazeTree.tree.getConnections(nextVertex)
            
            # Find adjacent vertices that have been visited to join
            mergeWith = []
            for vertex in adjacent:
                if vertex in visited:
                    # Potential vertex to merge with
                    mergeWith.append(vertex) 
                elif vertex not in frontiers:
                    # Add all new adjacent vertices to frontiers
                    frontiers.append(vertex) 
                    
            # Select vertex to merge with nextVertex
            mergeVertex = random.choice(mergeWith)
            
            visited.append(nextVertex)
            frontiers.remove(nextVertex)
            
            draw.mergeCells(nextVertex, mergeVertex, size)
            
            