import tkinter as tk

from logic.study.sqlalchemy.Deck import Deck
from ui.ColorConsts import ColorConsts
from ui.FontFamilyConsts import FontFamilyConsts

class DeckNameText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Frame, deck: Deck):
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14)
        )
        self.window = window
        self.configure(text = deck.start_position.name)
        self.pack(anchor = tk.W, padx = 10, pady = (10, 5))