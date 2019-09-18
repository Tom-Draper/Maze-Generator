class Graph():
    
    def __init__(self, displayDetail):
        self.displayDetail = displayDetail # Wether display updates to console 
        self.vertices = {}  # Vertices stored as {vertex1: {vertexConnected:weight, vertexConnected:weight}, 
                            #                     vertex2: {vertexConnected:weight},...}
                            # Example: {0:{1:4, 5:4}, 1:{0:4, 2:6, 6:3}, ...}

    # Add a vertex id given to vertices dictionary without any connections
    def addVertex(self, vertexID):
        # If vertex id not found, add vertex to vertices dict
        if vertexID in self.vertices.keys():
            if self.displayDetail: print('Vertex ID already exists.')
        else:
            self.vertices[vertexID] = {} # Add id with no connections
            
    # Remove a vertex id given and connections from the vertices dictionary
    def removeVertex(self, vertexID):
        # If vertex id found, remove vertex from vertices dictionary
        if vertexID in self.vertices.keys():
            del self.vertices[vertexID] 
            if self.displayDetail: print('Vertex removed.')
        else:
            if self.displayDetail: print('Vertex ' + str(vertexID) + ' not found.')
            
    # Add a weightless connection between two vertices given
    def addConnection(self, firstId, secondId):
        # If both vertices exist, add connection between the two
        if firstId in self.vertices.keys() and secondId in self.vertices.keys():
            # If no connection exists, add connection
            if not secondId in self.vertices[firstId]:
                self.vertices[firstId][secondId] = 1
                self.vertices[secondId][firstId] = 1
                if self.displayDetail: 
                    print('Added connection between vertex '+ str(firstId) + 
                          ' and ' + str(secondId) + '.')
            else:
                if self.displayDetail: 
                    print('There is already a connection between vertex '
                          + str(firstId) + ' and ' + str(secondId))
        else:
            if self.displayDetail: print('Vertex not found.')
            
    # Add a weighted connection between two vertices given
    def addWeightedConnection(self, firstId, secondId, weight):
        # If both vertices exist, add connection between the two
        if firstId in self.vertices.keys() and secondId in self.vertices.keys():
            # If no connection exists, add connection
            if not secondId in self.vertices[firstId]:
                self.vertices[firstId][secondId] = weight
                self.vertices[secondId][firstId] = weight
                if self.displayDetail:
                    print('Added weight ' + str(weight) + ' between vertex ' 
                          + str(firstId) + ' and ' + str(secondId) + '.')
            else:
                if self.displayDetail:
                    print('There is already a connection between vertex ' + 
                          str(firstId) + ' and ' + str(secondId))
        else:
            if self.displayDetail: print('Vertex not found.')
            
    # Remove a weighted or weightless connection between two vertices given
    def removeConnection(self, firstId, secondId):
        # If both vertices exist, remove connection between the two
        if firstId in self.vertices.keys() and secondId in self.vertices.keys():
            # If connection exists, remove connection
            if secondId in self.vertices[firstId]:
                del self.vertices[firstId][secondId]
                del self.vertices[secondId][firstId]
                if self.displayDetail:
                    print('Removed graph connection between vertex ' + str(firstId) 
                          + ' and ' + str(secondId) + '.')
            else:
                if self.displayDetail:
                    print('Connection doesn\'t exist between vertex ' + str(firstId)
                          + ' and ' + str(secondId) + '.')
        else:
            if self.displayDetail: print('Vertex not found.')
            
    # Check and returns whether a connection currently exists between two
    # vertices given
    def connectionExist(self, firstId, secondId):
        return (firstId in self.vertices.keys() and secondId in self.vertices.keys() and 
                secondId in self.vertices[firstId] and firstId in self.vertices[secondId])
            
    # Get and return a list of connections to a given vertex
    def getConnections(self, vertexID):
        connections = (tuple(self.vertices[vertexID].keys()))
    
        return list(connections)
            
    # Display each vertex ID in the graph and a list of its connections
    def displayGraph(self):
        if self.displayDetail:
            # Check if dictionary empty
            if self.vertices:
                print('\nVertices:')
            else:
                print('No vertices found.')
            
            # Print each vertex idand its connections
            for vertexID in self.vertices.keys():
                connections = self.vertices[vertexID]
                print(str(vertexID) + ': ' + str(connections))


    