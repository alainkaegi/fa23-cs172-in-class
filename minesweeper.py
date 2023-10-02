"""A program that implements the game minesweeper
on a square grid.

Two parameters control its behavior:
  SIZE: the size of the game board
  NUM_MINES: the number of mines to be placed
"""

import random
import stddraw

SIZE = 10
NUM_MINES = 10

def init(size, numMines):
    """Initialize the size x size grid with num_mines mines.
    
    Each position of the grid records the presence of a mine and
    whether the user has clicked on that position in the form a
    tuple."""
    minefield = [[(False, False) for j in range(size)] for i in range(size)]
    while numMines > 0:
        x = random.randrange(0, size)
        y = random.randrange(0, size)
        (m, _) = minefield[x][y]
        if not m:
            minefield[x][y] = (True, False)
            numMines -= 1
    return minefield

def count_neighboring_mines(minefield, x, y):
    """Count the number of the neiboring mines.

    Count the number of mines in the eight positions immediately near to
    coordinate (x, y).  This function assumes that there is no mine at
    coordinate (x, y).
    """
    size = len(minefield)
    count = 0
    xx = x - 1
    while xx < x + 2:
        yy = y - 1
        while yy < y + 2:
            if (xx >= 0 and xx < size and yy >= 0 and yy < size):
                (m, _) = minefield[xx][yy]
                if m:
                    count += 1
            yy += 1
        xx += 1
    return count

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
            elif m:
                stddraw.setPenColor(stddraw.RED)
                stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.3)
                stddraw.setPenColor(stddraw.BLACK)
            else:
                count = count_neighboring_mines(minefield, x, y)
                if count != 0:
                    stddraw.text(x*side + half, y*side + half, str(count))
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

def main():
    print('Welcome to minesweeper')
    minefield = init(SIZE, NUM_MINES)
    draw(minefield)
    while True:
        handleUser(minefield)
        draw(minefield)
        if (won(minefield)):
            print('You won!')
            stddraw.show()

if __name__ == '__main__': main()
