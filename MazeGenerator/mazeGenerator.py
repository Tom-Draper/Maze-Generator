from mazeTree import MazeTree
from drawMaze import DrawMaze
from mazeAlgorithms import MazeAlgorithms

size = 10

# Create initial maze weighted tree (grid)
mazeTree = MazeTree(size)
mazeTree.tree.displayTree() # Display vertices and connections

# Draw initial maze grid
draw = DrawMaze(size, pensize=3)

# Apply prim's algorithm to maze tree and display
algorithm = MazeAlgorithms()
algorithm.primsAlgorithm(size, mazeTree, draw)

mazeTree.tree.displayTree() # Display vertices and connections

draw.finish()