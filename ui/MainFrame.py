import tkinter

from ui.BoardCanvas import BoardCanvas

class MainFrame(tkinter.Frame):
    def __init__(self, master: tkinter.Tk) -> None:
        super().__init__(master)
        self.canvas = BoardCanvas(self)
        self.pack()