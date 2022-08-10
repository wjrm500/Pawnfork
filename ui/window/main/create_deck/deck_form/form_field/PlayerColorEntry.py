import tkinter as tk

from logic.consts.deck_positions import deck_positions
from logic.enums.Color import Color

class PlayerColorEntry(tk.OptionMenu):
    def __init__(self, window: tk.Tk, master: tk.Frame, option_var: tk.StringVar) -> None:
        super().__init__(
            master,
            option_var,
            *[Color.WHITE.value, Color.BLACK.value],
        )
        self.window = window
        self.option_var = option_var
        self.pack(anchor = tk.W, padx = 25, pady = (5, 10))