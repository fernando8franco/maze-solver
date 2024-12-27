from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    line = Line(Point(0, 1), Point(200, 200))
    win.draw_line(line)
    win.wait_for_close()

if __name__=="__main__":
    main()