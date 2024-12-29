from graphics import Window, Point
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(
        2,
        2,
        5,
        5,
        50,
        50,
        win
    )

    maze._create_cells()

    win.wait_for_close()

if __name__=="__main__":
    main()