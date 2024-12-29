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
            win
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

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(Cell(self.win))
            self._cells.append(row)

            for k in range(self.num_cols):
                self._draw_cell(i, k)

    def _draw_cell(self, i, k):
        cell = self._cells[i][k]

        x1 = (self.cell_size_x * k) + self.x1
        y1 = (self.cell_size_y * i) + self.y1
        x2 = self.cell_size_x + x1
        y2 = self.cell_size_y + y1
        
        cell.draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)