from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(Cell(self.win))
            self._cells.append(row)

            for k in range(self.num_cols):
                self._draw_cell(i, k)

    def _draw_cell(self, i, k):
        if not self.win:
            return

        x1 = (self.cell_size_x * k) + self.x1
        y1 = (self.cell_size_y * i) + self.y1
        x2 = self.cell_size_x + x1
        y2 = self.cell_size_y + y1
        
        self._cells[i][k].draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        if not self.win:
            return
        
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_rows - 1][self.num_cols - 1].has_right_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        while True:
            adjacent = []

            if j > 0 and not self._cells[i][j - 1]._visited:
                adjacent.append((i, j - 1))
            
            if j < self.num_cols - 1 and not self._cells[i][j + 1]._visited:
                adjacent.append((i, j + 1))

            if i > 0 and not self._cells[i - 1][j]._visited:
                adjacent.append((i - 1, j))

            if i < self.num_rows - 1 and not self._cells[i + 1][j]._visited:
                adjacent.append((i + 1, j))

            if not adjacent:
                self._draw_cell(i, j)
                return

            direction = adjacent[random.randrange(len(adjacent))]

            if direction[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            if direction[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            if direction[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            if direction[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False

            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self._cells[i][j]._visited:
                    self._cells[i][j]._visited = False