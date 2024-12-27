from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    win.wait_for_close()

if __name__=="__main__":
    main()