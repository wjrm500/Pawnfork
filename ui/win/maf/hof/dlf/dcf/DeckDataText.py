import tkinter as tk

from logic.study.sqlalchemy.Deck import Deck
from ui.ColorConsts import ColorConsts

class DeckDataText(tk.Text):
    def __init__(self, window: tk.Tk, master: tk.Frame, deck: Deck):
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR,
            borderwidth = 0,
            height = 1,
            font = ('Cambria', 10),
        )
        self.window = window
        deck_text = f'Colour: {deck.player_colour} - Turn Depth: {deck.turn_depth} - Response Depth: {deck.response_depth}'
        self.insert(tk.END, deck_text)
        self.config(state = tk.DISABLED)
        self.pack()