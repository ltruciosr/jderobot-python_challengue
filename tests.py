import unittest
import yaml
from board.tools import Board
from board.tools import Cell


class TestBoard(unittest.TestCase):
    """
    Class TestBoard inherits unittest.TestCase

    constructor holding Board object with parameters:
        rows: 15
        columns: 15
        live probability: 0.3
        random_seed: 0

    constructor holding Board basic:
        A:  [ ][x][ ]   B:  [x][x][x]   C:  [x][ ][x]   D:  [ ][ ][ ]
            [x][x][x]       [x][ ][x]       [ ][ ][ ]       [ ][ ][ ]
            [ ][x][ ]       [x][x][x]       [x][ ][x]       [ ][ ][ ]
    """

    def __init__(self, *args, **kwargs):
        super(TestBoard, self).__init__(*args, **kwargs)

        self.columns = 15
        self.rows = 15
        self.live_probability = 0.3
        self.random_seed = 0

        self.Board = Board(
            rows=self.rows,
            columns=self.columns,
            live_probability=self.live_probability,
            seed=self.random_seed,
        )

        self.A_board = Board(3, 3)
        self.B_board = Board(3, 3)
        self.C_board = Board(3, 3)

    def test_initialization(self):
        rows = len(self.Board.grid)
        columns = len(self.Board.grid[0])
        alive_cells = self.Board.get_alives_count()

        self.assertEqual(rows, self.rows)
        self.assertEqual(columns, self.columns)
        self.assertEqual(alive_cells, 57)

    def test_rules(self):
        # init boards
        self.A_board.grid = [
            [Cell(False), Cell(True), Cell(False)],
            [Cell(True), Cell(True), Cell(True)],
            [Cell(False), Cell(True), Cell(False)],
        ]

        self.B_board.grid = [
            [Cell(True), Cell(True), Cell(True)],
            [Cell(True), Cell(False), Cell(True)],
            [Cell(True), Cell(True), Cell(True)],
        ]

        self.C_board.grid = [
            [Cell(True), Cell(False), Cell(True)],
            [Cell(False), Cell(False), Cell(False)],
            [Cell(True), Cell(False), Cell(True)],
        ]

        # get alive cells count
        A_alive_cells = self.A_board.get_alives_count()
        B_alive_cells = self.B_board.get_alives_count()
        C_alive_cells = self.C_board.get_alives_count()

        self.assertEqual(A_alive_cells, 5)
        self.assertEqual(B_alive_cells, 8)
        self.assertEqual(C_alive_cells, 4)

        # update board
        self.A_board.update_board()
        self.B_board.update_board()
        self.C_board.update_board()

        A_alive_cells = self.A_board.get_alives_count()
        B_alive_cells = self.B_board.get_alives_count()
        C_alive_cells = self.C_board.get_alives_count()

        self.assertEqual(A_alive_cells, 8)
        self.assertEqual(B_alive_cells, 4)
        self.assertEqual(C_alive_cells, 0)


if __name__ == "__main__":
    unittest.main()