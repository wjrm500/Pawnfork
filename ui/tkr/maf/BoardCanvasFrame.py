import tkinter as tk
from ui.ColorConsts import ColorConsts

from ui.tkr.maf.bcf.BoardCanvas import BoardCanvas

class BoardCanvasFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR
        )
        self.canvas = BoardCanvas(self)
        self.pack(fill = tk.BOTH, expand = True)