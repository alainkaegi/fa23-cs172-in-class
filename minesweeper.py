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

def draw(minefield):
    stddraw.clear()
    size = len(minefield)
    side = 1.0/size
    half = side/2.0
    for x in range(size):
        for y in range(size):
            (m, r) = minefield[x][y]
            if (not r):
                stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
                stddraw.filledSquare(x*side + half, y*side + half, half)
                stddraw.setPenColor(stddraw.BLACK)
            stddraw.square(x*side + half, y*side + half, half)
    stddraw.show(0)

def reveal(minefield, x, y):
    (m, _) = minefield[x][y]
    minefield[x][y] = (m, True)

def handleUser(minefield):
    size = len(minefield)
    side = 1.0/size
    half = side/2.0

    while not stddraw.mousePressed():
        stddraw.show(1)

    xx = stddraw.mouseX()
    yy = stddraw.mouseY()
    x = round((xx - half)/side)
    y = round((yy - half)/side)

    while stddraw.mousePressed():
        None # do nothing

    reveal(minefield, x, y)

    (m, _) = minefield[x][y]
    if m:
        print('BOOM')

def won(minefield):
    return False

SIZE = 10
NUM_MINES = 10

print('Welcome to minesweeper')
minefield = init(SIZE, NUM_MINES)
draw(minefield)
while True:
    handleUser(minefield)
    draw(minefield)
    if (won(minefield)):
        print('You won!')
        stddraw.show()
