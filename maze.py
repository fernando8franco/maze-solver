from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

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
        self._cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)