import tkinter

from ui.tkr.maf.bcf.BoardCanvas import BoardCanvas

class BoardCanvasFrame(tkinter.Frame):
    def __init__(self, master: tkinter.Tk) -> None:
        super().__init__(master)
        self.canvas = BoardCanvas(self)
        self.pack()