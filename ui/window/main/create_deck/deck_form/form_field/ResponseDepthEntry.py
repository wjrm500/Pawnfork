import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class ResponseDepthEntry(tk.Entry):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12)
        )
        self.window = window
        self.pack(anchor = tk.W, padx = 25, pady = (5, 10))