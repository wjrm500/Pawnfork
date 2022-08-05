import tkinter as tk
from ui.ColorConsts import ColorConsts

from ui.win.maf.stf.BoardCanvas import BoardCanvas

class StudyFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR
        )
        self.window = window
        self.canvas = BoardCanvas(self.window, self)
        self.pack(fill = tk.BOTH, expand = True)