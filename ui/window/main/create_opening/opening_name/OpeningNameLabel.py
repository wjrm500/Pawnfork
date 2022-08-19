import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class OpeningNameLabel(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12)
        )
        self.window = window
        self.configure(text = 'Opening name:')
        self.pack(side = tk.LEFT, padx = (10, 5), pady = 10)