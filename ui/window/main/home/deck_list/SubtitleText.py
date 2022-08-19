import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class SubtitleText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 16)
        )
        self.window = window
        text = 'You have no decks.' if self.window.database.get_decks() == [] else 'Click a deck to study!'
        self.configure(text = text)
        self.pack(anchor = tk.W, padx = 15, pady = (15, 0))