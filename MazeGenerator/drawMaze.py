import turtle

class DrawMaze():
    
    def __init__(self, size):
        self.drawInitialGrid(size)
        
    def drawInitialGrid(self, size):
        wn = turtle.Screen()
        wn.title("Maze")
        wn.bgcolor("white")
        wn_width = 1000
        wn_height = 1000
        wn.setup(wn_width, wn_height)
        
        # Set up drawing tool
        pen = turtle.Turtle()
        pen.color("black")
        pen.hideturtle()
        pen.speed(0)
        pen.pensize(3)
        turtle.tracer(False)
        
        startX = -((wn_width-100)/2)
        startY = (wn_height-100)/2
        cellLength = ((wn_width-100)/size)
        
        # Draw horizontal lines
        for count in range(size + 1):
            pen.up()
            pen.goto(startX, startY - (count * cellLength))
            pen.down()
            forward = size * cellLength
            pen.forward(forward)
            
        pen._rotate(270)
            
        # Draw vertical lines
        for count in range(size + 1):
            pen.up()
            pen.goto(startX + (count * cellLength), startY )
            pen.down()
            forward = size * cellLength
            pen.forward(forward)
        
        turtle.update()
        turtle.done()