import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class SubtitleText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 16)
        )
        self.window = window
        self.configure(text = 'Create new deck')
        self.pack(anchor = tk.W, padx = 25, pady = (25, 0))