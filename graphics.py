from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, win=None):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill = BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win=None):
        if self.__win is None:
            return
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            l = Line(Point(self.__x1,self.__y1), Point(self.__x1,self.__y2))
            self.__win_draw_line(l)
        
        if self.has_right_wall:
            l = Line(Point(self.__x2,self.__y1), Point(self.__x2,self.__y2))
            self.__win_draw_line(l)
        
        if self.has_top_wall:
            l = Line(Point(self.__x1,self.__y1), Point(self.__x2,self.__y1))
            self.__win_draw_line(l)
        
        if self.has_bottom_wall:
            l = Line(Point(self.__x1,self.__y2), Point(self.__x2,self.__y2))
            self.__win_draw_line(l)
        