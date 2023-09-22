"""A program that implements the game minesweeper
on a square grid.

Two parameters control its behavior:
  SIZE: the size of the game board
  NUM_MINES: the number of mines to be placed
"""

import random
import stddraw
import stdarray

def init(size, numMines):
    """Initialize the size x size grid with num_mines mines.
    
    Each position of the grid records the presence of a mine and
    whether the user has clicked on that position in the form a
    tuple."""
    minefield = stdarray.create2D(size, size, (False, False))
    while numMines > 0:
        x = random.randrange(0, size)
        y = random.randrange(0, size)
        (m, _) = minefield[x][y]
        if not m:
            minefield[x][y] = (True, False)
            numMines -= 1
    return minefield


SIZE = 10
NUM_MINES = 10


print('Welcome to minesweeper')
minefield = init(SIZE, NUM_MINES)
draw(minefield)



stddraw.filledCircle(.5, .5, 0.3)
stddraw.show()
