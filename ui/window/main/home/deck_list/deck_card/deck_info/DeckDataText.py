import tkinter as tk

from logic.study.sqlalchemy.Deck import Deck
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class DeckDataText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Widget, deck: Deck) -> None:
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 10)
        )
        self.window = window
        deck_text = f'Color: {deck.player_color} - Turn Depth: {deck.turn_depth} - Response Depth: {deck.response_depth} - Size: {len(deck.flashcards)}'
        self.configure(text = deck_text)
        self.pack(anchor = tk.W, padx = 10, pady = (5, 10))