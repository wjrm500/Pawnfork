import tkinter as tk
from ui.ColorConsts import ColorConsts

from ui.win.maf.stf.BoardCanvas import BoardCanvas

class StudyFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR
        )
        self.canvas = BoardCanvas(self)
        self.pack(fill = tk.BOTH, expand = True)