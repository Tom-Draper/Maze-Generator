from mazeTree import MazeTree
from drawMaze import DrawMaze
from mazeAlgorithms import MazeAlgorithms

size = 50

mazeTree = MazeTree(size)
mazeTree.tree.displayTree()

draw = DrawMaze(size, pensize=3)

algorithm = MazeAlgorithms()
algorithm.primsAlgorithm(size, mazeTree, draw)

draw.finish()

