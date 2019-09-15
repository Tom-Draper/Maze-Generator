import turtle

class DrawMaze():
    
    def __init__(self, size):
        self.wn = turtle.Screen()
        self.pen = turtle.Turtle()
        
        self.wn_width = 1000
        self.wn_height = 1000
        
        self.pensize = 3
        
        self.startX = -((self.wn_width-100)/2)
        self.startY = (self.wn_height-100)/2
        
        self.cellLength = ((self.wn_width-100)/size)
        
        self.drawInitialGrid(size)
        
    def drawInitialGrid(self, size):
        
        self.wn.title("Maze")
        self.wn.bgcolor("white")
        
        self.wn.setup(self.wn_width, self.wn_height)
        
        # Set up drawing tool
        self.pen.color("black")
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(self.pensize)
        turtle.tracer(False)
        
        # Draw horizontal lines
        for count in range(size + 1):
            self.pen.up()
            self.pen.goto(self.startX, self.startY - (count * self.cellLength))
            self.pen.down()
            forward = size * self.cellLength
            self.pen.forward(forward)
            
        self.pen._rotate(270)
            
        # Draw vertical lines
        for count in range(size + 1):
            self.pen.up()
            self.pen.goto(self.startX + (count * self.cellLength), self.startY )
            self.pen.down()
            forward = size * self.cellLength
            self.pen.forward(forward)
        
        turtle.update()
        
    def removeEdge(self, X1, Y1, X2, Y2):
        self.pen = turtle.Turtle()
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.hideturtle()
        
        self.pen.up()
        self.pen.goto(X1, Y1)
        self.pen.down()
        self.pen.goto(X2, Y2)
        
        turtle.update()
        
    def createExit(self, vertex, size, edge):
        # Get location vertex by length along edge either right or down 
            # (depending on edge)
        if edge == 't':
            location = vertex
            X1 = self.startX + location * self.cellLength + self.pensize
            X2 = X1 + self.cellLength - self.pensize
            Y1 = Y2 = self.startY
        elif edge == 'b':
            location = vertex - (size*(size-1))
            X1 = self.startX + (location * self.cellLength) + self.pensize
            X2 = X1 + self.cellLength - self.pensize
            Y1 = Y2 = self.startY - (self.cellLength * size)
        elif edge == 'l':
            location = vertex / size
            X1 = X2 = self.startX
            Y1 = self.startY - (location * self.cellLength) - self.pensize
            Y2 = Y1 - self.cellLength + self.pensize
        elif edge == 'r':
            location = (vertex - (size - 1)) / size + 1
            X1 = X2 = self.startX + (self.cellLength * size)
            Y1 = self.startY - (location * self.cellLength) - self.pensize
            Y2 = Y1 + self.cellLength + self.pensize
            
        self.removeEdge(X1, Y1, X2, Y2)
            
    def getTopLeftCornerXCoords(self, vertexID, size):
        return self.startX + (self.cellLength * ((vertexID + size) % size))
        
    def getTopLeftCornerYCoords(self, vertexID, size):
        return self.startY - (self.cellLength * (vertexID//size))
            
    def mergeCells(self, nextVertex, mergeVertex, size):
        # Get coordinates of top left corner of vertex cell
        nextVertexXCoord = self.getTopLeftCornerXCoords(nextVertex, size)
        nextVertexYCoord = self.getTopLeftCornerYCoords(nextVertex, size)
        mergeVertexXCoord = self.getTopLeftCornerXCoords(mergeVertex, size)
        mergeVertexYCoord = self.getTopLeftCornerYCoords(mergeVertex, size)
        
        '''
        self.pen.up()
        self.pen.goto(nextVertexXCoord, nextVertexYCoord)
        self.pen.color("green")
        self.pen.down()
        self.pen.goto(mergeVertexXCoord, mergeVertexYCoord)
        
        turtle.update()
        '''
        
        # Get edge the of nextVertex cell that mergeVertex is adjacent.
        # mergeVertex above nextVertex
        if nextVertex == mergeVertex + size:
            # Top left corner of nextVertex
            X1 = nextVertexXCoord + self.pensize
            Y1 = nextVertexYCoord
            # Bottom right corner of mergeVertex
            X2 = mergeVertexXCoord + self.cellLength - self.pensize
            Y2 = mergeVertexYCoord - self.cellLength
            self.removeEdge(X1, Y1, X2, Y2)
        # mergeVertex below nextVertex
        elif nextVertex + size == mergeVertex:
            # Bottom left corner of nextVertex
            X1 = nextVertexXCoord + self.pensize
            Y1 = nextVertexYCoord - self.cellLength
            # Top right corner of mergeVertex
            X2 = mergeVertexXCoord + self.cellLength - self.pensize
            Y2 = mergeVertexYCoord
            self.removeEdge(X1, Y1, X2, Y2)
        # mergeVertex to left of nextVertex
        elif nextVertex == mergeVertex + 1:
            # Top left corner of nextVertex
            X1 = nextVertexXCoord
            Y1 = nextVertexYCoord - self.pensize
            # Bottom right corner of mergeVertex
            X2 = mergeVertexXCoord + self.cellLength
            Y2 = mergeVertexYCoord - self.cellLength + self.pensize
            self.removeEdge(X1, Y1, X2, Y2)
        # mergeVertex to right of nextVertex
        elif nextVertex + 1 == mergeVertex:
            # Top right corner of nextVertex
            X1 = nextVertexXCoord + self.cellLength
            Y1 = nextVertexYCoord - self.pensize
            # Bottom left corner of mergeVertex
            X2 = mergeVertexXCoord
            Y2 = mergeVertexYCoord - self.cellLength + self.pensize
            self.removeEdge(X1, Y1, X2, Y2)
            
        print('Removed edge between ' + str(nextVertex) + ' and ' + 
              str(mergeVertex) + '.') 
    
    def finish(self):
        turtle.done()