import sys
from mazeTree import MazeTree
from drawMaze import DrawMaze
from primsAlgorithm import PrimsAlgorithm

# Defaults
size = 100
display = True

# Get any command line inputs
for arg in range(len(sys.argv)):
    if sys.argv[arg].lower() == 'true':
        display = True
    elif sys.argv[arg].lower() == 'false':
        disply = False
    elif sys.argv[arg].isdigit():
        size = int(sys.argv[arg])
    
# Create initial maze weighted tree (grid)
mazeTree = MazeTree(size, display)
mazeTree.tree.displayTree() # Display vertices and connections

# Draw initial maze grid
draw = DrawMaze(size, 3, display)

# Apply prim's algorithm to maze tree and display
primsAlgorithm = PrimsAlgorithm(mazeTree, draw)
primsAlgorithm.run()

mazeTree.tree.displayTree() # Display vertices and connections

draw.finish()