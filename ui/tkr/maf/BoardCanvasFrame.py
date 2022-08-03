import tkinter as tk

from ui.tkr.maf.bcf.BoardCanvas import BoardCanvas

class BoardCanvasFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.canvas = BoardCanvas(self)
        self.pack()