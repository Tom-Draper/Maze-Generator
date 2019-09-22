# mazeGenerator.py - the main program to run. Creates a maze graph and runs an
# algorithm on the graph to form a maze. Allows user inputs of size of the maze
# and whether to display generation details to console.

import sys
from progressBar import ProgressBar
from mazeGraph import MazeGraph
from drawMaze import DrawMaze
from primsAlgorithm import PrimsAlgorithm

# Defaults
size = 50
# If true, written details of progress displayed to console.
# If false, simple progress bar displayed.
displayDetail = False
pensize = 2
progBarUpdateFreq = 30 # 1 out of 'progBarUpdateFreq' chance to update

gotSizeInput = False
# Get any command line inputs to overwrite size and displayDetail
for arg in range(len(sys.argv)):
    if sys.argv[arg].lower() == 'true':
        displayDetail = True
    elif sys.argv[arg].lower() == 'false':
        displyDetail = False
    elif sys.argv[arg].isdigit():
        size = int(sys.argv[arg])
        gotSizeInput = True
      
# If size argument not found, get command line entry  
if gotSizeInput == False:
    enteredSize = input('Enter size of maze: ')
    if enteredSize.isdigit():
        size = int(enteredSize)
    else:
        print('Invalid size: taking default of ' + str(size))
        
# Create a progress bar object ready for graph creation.
progressBar = ProgressBar(displayDetail, progBarUpdateFreq)

# Create initial maze weighted graph (grid of connected vertices).
mazeGraph = MazeGraph(size, displayDetail, progressBar)
mazeGraph.graph.displayGraph() # Display vertices and connections

# Draw initial maze grid
draw = DrawMaze(size, pensize, displayDetail)

# Apply prim's algorithm to maze graph and display
primsAlgorithm = PrimsAlgorithm(mazeGraph, draw)
primsAlgorithm.run()

mazeGraph.graph.displayGraph() # Display vertices and connections
draw.finish()