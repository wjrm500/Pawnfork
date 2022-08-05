import tkinter as tk

from logic.study.sqlalchemy.Deck import Deck
from ui.ColorConsts import ColorConsts
from ui.FontFamilyConsts import FontFamilyConsts

class DeckDataText(tk.Text):
    def __init__(self, window: tk.Tk, master: tk.Frame, deck: Deck):
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 10)
        )
        self.window = window
        deck_text = f'Colour: {deck.player_colour} - Turn Depth: {deck.turn_depth} - Response Depth: {deck.response_depth}'
        self.insert(tk.END, deck_text)
        self.config(state = tk.DISABLED)
        self.pack(anchor = tk.W, padx = 10, pady = (5, 10))