from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, title):
        self.root_widget = Tk()
        self.root_widget.title(title)
        self.canvas_widget = Canvas()
        self.canvas_widget.pack()
        self.window_running = False