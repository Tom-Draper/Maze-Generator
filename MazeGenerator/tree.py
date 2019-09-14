from vertex import Vertex

class Tree():
    
    def __init__(self):
        self.vertices = []

    def addVertex(self, id, value):
        if self.vertices.contains("vertex{0}".format(id)):
            print('Vertex ID already exists.')
        else:
            self.vertices.append({"vertex{0}".format(id): value})
            
    def removeVertex(self, id, value):
        if self.vertices.contains("vertex{0}".format(id)):
            self.vertices.remove("vertiex{0}".format(id))
            print('Vertex removed.')
        else:
            print('Vertex doesn\'t exist.')
    