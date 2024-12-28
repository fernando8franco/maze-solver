from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell2 = Cell(win)
    cell.draw(50, 50, 100, 100)
    cell2.draw(100, 50, 150, 100)

    cell.draw_move(cell2)

    win.wait_for_close()

if __name__=="__main__":
    main()