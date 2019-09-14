from vertex import Vertex

class Tree():
    
    def __init__(self):
        self.vertices = {}  # Example: {0(ID) : {1(vertexID):4(weight), 5(vertexID):4(weight)}, 
                            #           1 : {0:4, 2:6, 6:3}, ...}

    def addVertex(self, vertexID):
        # If vertex id not found, add vertex to vertices dict
        if vertexID in self.vertices.keys():
            print('Vertex ID already exists.')
        else:
            self.vertices[vertexID] = {} # Add id with no connections
            
    def removeVertex(self, vertexID):
        # If vertex id found, remove vertex from vertices dict
        if vertexID in self.vertices.keys():
            del self.vertices[vertexID]
            print('Vertex removed.')
        else:
            print('Vertex ' + str(vertexID) + ' not found.')
            
    def addConnection(self, firstId, secondId):
        # If both vertices exist, add connection between the two
        if firstId in self.vertices.keys() and secondId in self.vertices.keys():
            # If no connection exists, add connection
            if not secondId in self.vertices[firstId]:
                self.vertices[firstId][secondId] = 1
                self.vertices[secondId][firstId] = 1
                print('Added connection between vertex ' + str(firstId) + ' and ' 
                      + str(secondId) + '.')
            else:
                print('There is already a connection between vertex ' + 
                      str(firstId) + ' and ' + str(secondId))
        else:
            print('Vertex not found.')
            
    def addWeightedConnection(self, firstId, secondId, weight):
        # If both vertices exist, add connection between the two
        if firstId in self.vertices.keys() and secondId in self.vertices.keys():
            # If no connection exists, add connection
            if not secondId in self.vertices[firstId]:
                self.vertices[firstId][secondId] = weight
                self.vertices[secondId][firstId] = weight
                print('Added weight ' + str(weight) + ' between vertex ' 
                    + str(firstId) + ' and ' + str(secondId) + '.')
            else:
                print('There is already a connection between vertex ' + 
                      str(firstId) + ' and ' + str(secondId))
        else:
            print('Vertex not found.')
            
    def removeConnection(self, firstId, secondId):
        # If both vertices exist, remove connection between the two
        if firstId in self.vertices.keys() and secondId in self.vertices.keys():
            # If connection exists, remove connection
            if secondId in self.vertices[firstId]:
                del self.vertices[firstId][secondId]
                del self.vertices[secondId][firstId]
                print('Removed connection between vertex ' + str(firstId) + ' and ' 
                      + str(secondId) + '.')
            else:
                print('Connection doesn\'t exist between vertex ' + str(firstId)
                      + str(secondId) + '.')
        else:
            print('Vertex not found.')
            
    def connectionExist(self, firstId, secondId):
        if (firstId in self.vertices.keys() and secondId in self.vertices.keys() and 
                secondId in self.vertices[firstId]):
            return True
            
    def displayTree(self):
        # Check if dictionary empty
        if self.vertices:
            print('Vertices:')
        else:
            print('No vertices found.')
        
        # Print each vertex idand its connections
        for vertexID in self.vertices.keys():
            connections = self.vertices[vertexID]
            print(str(vertexID) + ': ' + str(connections))


    