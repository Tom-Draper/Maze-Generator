# Maze-Generator
 
This project generates a random maze of a selected size and visualises the process. I started this project to graps some of the algorithms used for maze generation and visualise the steps an algorithm takes. Currently only Prim's Algorithm is implemented.

### Demo - Prim's Algorithm (20x20)

[![Demo Prim's Algorithm](https://media.giphy.com/media/S44bVOtLqbP49oyGPT/giphy.gif)](https://www.youtube.com/watch?v=lCfpZhXvS_Q)

#### Project Aims:
- Understand and implement a maze generation
- Expand Python GUI skills

#### What I Learned:
- General background of maze generation
- Details and method of Prim's Algorithm

In future, I aim to increase the number of algorithms in this implementation as alternatives to Prim's Algorithm. For a future project I could extend this program to implement a playable maze game. I will need to revist the implementationa to improve efficiency as currently walls are removed by drawing over a wall with a line of the background colour. Using an alternative to Python's Turtle module could allow for more control over placing and removing walls and subsequently allow for a variable animation playback speed. As this project centred around the visualisation aspect, the effeciency of the display wasn't top priority. 

-------------------------------------------------------

## Getting Started
Run mazeGenerator.py to begin maze generation.

#### Optional command line arguments:
- Size (-s int_value) - integer length of one side of the maze. Size defaults to 50 (50x50 maze).  
- Display details (-d true/false) - If true, details of generation prints to console. If false, progress bar displayed in console instead. Display details defaults to false.
