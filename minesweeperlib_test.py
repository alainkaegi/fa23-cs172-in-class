import minesweeperlib

def test_count_neighboring_mines():
    minefield = [[(True,  False), (True,  False), (False, False)],
                 [(False, False), (False, False), (False, False)],
                 [(False, False), (False, False), (False, False)]]
    assert minesweeperlib.count_neighboring_mines(minefield, 1, 0) == 2
    assert minesweeperlib.count_neighboring_mines(minefield, 2, 2) == 0
