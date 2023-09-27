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
