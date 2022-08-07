import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class TitleText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.TITLE_FONT_FAMILY, 48),
        )
        self.window = window
        self.configure(text = 'Pawnfork')
        self.pack(anchor = tk.CENTER)