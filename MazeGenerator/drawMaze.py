import turtle

# Holds the functionality to draw a maze using the Turtle module
# Draws an initial grid of input dimensions
# Removes select lines
class DrawMaze():
    
    def __init__(self, size, pensize, displayDetail):
        self.size = size # Length of (size x size) maze
        self.pensize = pensize
        self.displayDetail = displayDetail
        
        self.wn = turtle.Screen()
        self.pen = turtle.Turtle()
        
        self.wn_width = 1000
        self.wn_height = 1000
        self.penColour = 'black'
        self.bgColour = 'white'
        
        self.startX = -((self.wn_width-100)/2)
        self.startY = (self.wn_height-100)/2
        
        self.cellLength = ((self.wn_width-100)/size)
        
        self.drawInitialGrid()
        
    # Draw the intial maze grid
    def drawInitialGrid(self):
        # Set up window
        self.wn.title("Maze")
        self.wn.bgcolor(self.bgColour)
        self.wn.setup(self.wn_width, self.wn_height)
        
        # Set up drawing tool
        self.pen.color(self.penColour)
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(self.pensize)
        turtle.tracer(False)
        
        # Draw horizontal lines
        for count in range(self.size + 1):
            self.pen.up()
            self.pen.goto(self.startX, self.startY - (count * self.cellLength))
            self.pen.down()
            forward = self.size * self.cellLength
            self.pen.forward(forward)
            
        self.pen._rotate(270)
            
        # Draw vertical lines
        for count in range(self.size + 1):
            self.pen.up()
            self.pen.goto(self.startX + (count * self.cellLength), self.startY)
            self.pen.down()
            forward = self.size * self.cellLength
            self.pen.forward(forward)
        
        turtle.update()
        
    # Draw line in background colour to remove edge
    # Coodrinates of end of line to draw input 
    def removeEdge(self, X1, Y1, X2, Y2):
        self.pen = turtle.Turtle()
        self.pen.color(self.bgColour)
        self.pen.pensize(self.pensize)
        self.pen.hideturtle()
        
        # Erase line
        self.pen.up()
        self.pen.goto(X1, Y1)
        self.pen.down()
        self.pen.goto(X2, Y2)
        
        turtle.update()
        
    # Remove edge adjacent to vertex given to create gap in outer wall
    def createExit(self, vertex, edge):
        # Get location vertex by length along edge either right or down 
        # (depending on edge)
        if edge == 't':
            location = vertex
            X1 = self.startX + location * self.cellLength + self.pensize
            X2 = X1 + self.cellLength - self.pensize
            Y1 = Y2 = self.startY
        elif edge == 'b':
            location = vertex - (self.size * (self.size - 1))
            X1 = self.startX + (location * self.cellLength) + self.pensize
            X2 = X1 + self.cellLength - self.pensize
            Y1 = Y2 = self.startY - (self.cellLength * self.size)
        elif edge == 'l':
            location = vertex / self.size
            X1 = X2 = self.startX
            Y1 = self.startY - (location * self.cellLength) - self.pensize
            Y2 = Y1 - self.cellLength + self.pensize
        elif edge == 'r':
            location = (vertex - (self.size - 1)) / self.size + 1
            X1 = X2 = self.startX + (self.cellLength * self.size)
            Y1 = self.startY - (location * self.cellLength) - self.pensize
            Y2 = Y1 + self.cellLength + self.pensize
            
        self.removeEdge(X1, Y1, X2, Y2)
            
    # Return the x coordinate of the top left corner of a particular vertex/maze cell
    def getTopLeftCornerXCoords(self, vertexID):
        return self.startX + (self.cellLength * ((vertexID + self.size) % self.size))
        
    # Return the y coordinate of the top left corner of a particular vertex/maze cell
    def getTopLeftCornerYCoords(self, vertexID):
        return self.startY - (self.cellLength * (vertexID//self.size))
            
    # Removes line between two vertices/maze cells
    # First gets coordinates of top left of both cells
    # Then determines how both vertices are adjacent (above/below or left/right)
    # Finally removes the edge between them based on this
    def mergeCells(self, nextVertex, mergeVertex):
        # Get coordinates of top left corner of vertex cell
        nextVertexXCoord = self.getTopLeftCornerXCoords(nextVertex)
        nextVertexYCoord = self.getTopLeftCornerYCoords(nextVertex)
        mergeVertexXCoord = self.getTopLeftCornerXCoords(mergeVertex)
        mergeVertexYCoord = self.getTopLeftCornerYCoords(mergeVertex)
        
        # Get edge the of nextVertex cell that mergeVertex is adjacent.
        # mergeVertex above nextVertex
        if nextVertex == mergeVertex + self.size:
            # Top left corner of nextVertex
            X1 = nextVertexXCoord + self.pensize
            Y1 = nextVertexYCoord
            # Bottom right corner of mergeVertex
            X2 = mergeVertexXCoord + self.cellLength - self.pensize
            Y2 = mergeVertexYCoord - self.cellLength
            self.removeEdge(X1, Y1, X2, Y2)
        # mergeVertex below nextVertex
        elif nextVertex + self.size == mergeVertex:
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
            
        # If display enabled, display update
        if self.displayDetail:
            print('Erased maze edge between ' + str(nextVertex) + ' and ' + 
                  str(mergeVertex) + '.') 
    
    # Stop and keep window open
    def finish(self):
        turtle.done()