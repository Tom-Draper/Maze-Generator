from mazeTree import MazeTree
from drawMaze import DrawMaze
from mazeAlgorithms import MazeAlgorithms

size = 5

mazeTree = MazeTree(size)
mazeTree.tree.displayTree()

draw = DrawMaze(size)

algorithm = MazeAlgorithms()
algorithm.primsAlgorithm(size, mazeTree, draw)

draw.finish()

