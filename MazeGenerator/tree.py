from vertex import Vertex

class Tree():
    
    def __init__(self):
        self.vertices = {}  # Example: {0 : {1:4, 5:4}, 1 : {0:4, 2:6, 6:3}, ...}

    def addVertex(self, id):
        if id in self.vertices.keys():
            print('Vertex ID already exists.')
        else:
            self.vertices[id] = {} # Add id with no connections
            
    def removeVertex(self, id):
        if id in self.vertices.keys():
            del self.vertices[id]
            print('Vertex removed.')
        else:
            print('Vertex ' + str(id) + ' not found.')
            
    def addConnection(self, firstId, secondId, weight):
        if firstId in self.vertices.keys() and secondId in self.vertices.keys():
            self.vertices[firstId][secondId] = weight
            self.vertices[secondId][firstId] = weight
            print('Added weight ' + str(weight) + ' between vertex ' 
                  + str(firstId) + ' and ' + str(secondId) + '.')
        else:
            print('Vertex not found.')
            
    def removeConnection(self, firstId, secondId):
        if firstId and secondId in self.vertices.keys():
            del self.vertices[firstId][secondId]
            del self.vertices[secondId][firstId]
            print('Removed connection between vertex ' + str(firstId) + ' and ' 
                  + str(secondId) + '.')
        else:
            print('Vertex not found.')
            
    def displayTree(self):
        # Check if dictionary empty
        if self.vertices:
            print('Vertices:')
        else:
            print('No vertices found.')
        
        # Print each vertex id and its connections
        for id in self.vertices.keys():
            connections = self.vertices[id]
            print(str(id) + ': ' + str(connections))

    