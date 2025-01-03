import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_right_wall,
            False,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows - 1][num_cols - 1].has_right_wall,
            False,
        )

    def test_reset_cells_visited(self):
        num_cols = 4
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertEqual(
                    m1._cells[i][j]._visited,
                    False,
                )

    def test_resolve(self):
        num_cols = 12
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 8)
        self.assertEqual(
            m1.solve(),
            True,
        )
                

if __name__ == "__main__":
    unittest.main()