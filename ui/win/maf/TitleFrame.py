import tkinter as tk

from ui.win.maf.tif.TitleText import TitleText
from ui.ColorConsts import ColorConsts

class TitleFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR,
            height = 1,
            pady = 25
        )
        self.window = window
        self.text = TitleText(self.window, self)
        self.pack(fill = tk.X)