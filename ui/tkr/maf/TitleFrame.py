import tkinter as tk

from ui.tkr.maf.tif.TitleText import TitleText
from ui.ColorConsts import ColorConsts

class TitleFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR,
            height = 1,
            pady = 25
        )
        self.text = TitleText(self)
        self.pack(fill = tk.X)