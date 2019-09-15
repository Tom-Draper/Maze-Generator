from mazeTree import MazeTree
from drawMaze import DrawMaze
from mazeAlgorithms import MazeAlgorithms

size = 10

mazeTree = MazeTree(size)
mazeTree.tree.displayTree()

draw = DrawMaze(size)

draw.createExit(1, 10, 't')
draw.createExit(19, 10, 'r')
draw.createExit(10, 10, 'l')

#algorithm = MazeAlgorithms()
#algorithm.primsAlgorithm(size, mazeTree, draw)

