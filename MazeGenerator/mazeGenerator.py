import sys
from progressBar import ProgressBar
from mazeGraph import MazeGraph
from drawMaze import DrawMaze
from primsAlgorithm import PrimsAlgorithm

# Defaults
size = 50
displayDetail = False

# Get any command line inputs
for arg in range(len(sys.argv)):
    if sys.argv[arg].lower() == 'true':
        displayDetail = True
    elif sys.argv[arg].lower() == 'false':
        displyDetail = False
    elif sys.argv[arg].isdigit():
        size = int(sys.argv[arg])
        
# Create a progress bar for the graph creation
progressBar = ProgressBar(displayDetail, updateFreq=20)

# Create initial maze weighted graph (grid)
mazeGraph = MazeGraph(size, displayDetail, progressBar)
mazeGraph.graph.displayGraph() # Display vertices and connections

# Draw initial maze grid
draw = DrawMaze(size, 3, displayDetail)

# Apply prim's algorithm to maze graph and display
primsAlgorithm = PrimsAlgorithm(mazeGraph, draw)
primsAlgorithm.run()

mazeGraph.graph.displaygraph() # Display vertices and connections

draw.finish()