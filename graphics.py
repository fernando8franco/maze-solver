from tkinter import Tk, BOTH, Canvas

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y, fill=fill_color, width=2
        )

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver 🐍")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

        print("Window closed")

    def close(self):
        self.__running = False