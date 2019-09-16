import sys
from progressBar import ProgressBar
from mazeTree import MazeTree
from drawMaze import DrawMaze
from primsAlgorithm import PrimsAlgorithm

# Defaults
size = 15
displayDetail = False

# Get any command line inputs
for arg in range(len(sys.argv)):
    if sys.argv[arg].lower() == 'true':
        displayDetail = True
    elif sys.argv[arg].lower() == 'false':
        displyDetail = False
    elif sys.argv[arg].isdigit():
        size = int(sys.argv[arg])
    
progressBar = ProgressBar(displayDetail, updateFreq=30)

# Create initial maze weighted tree (grid)
mazeTree = MazeTree(size, displayDetail, progressBar)
mazeTree.tree.displayTree() # Display vertices and connections

# Draw initial maze grid
draw = DrawMaze(size, 3, displayDetail)

# Apply prim's algorithm to maze tree and display
primsAlgorithm = PrimsAlgorithm(mazeTree, draw)
primsAlgorithm.run()

mazeTree.tree.displayTree() # Display vertices and connections

draw.finish()