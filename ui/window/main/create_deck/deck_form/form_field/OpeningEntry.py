import tkinter as tk

from logic.consts.deck_positions import deck_positions

class OpeningEntry(tk.OptionMenu):
    def __init__(self, window: tk.Tk, master: tk.Frame, option_var: tk.StringVar) -> None:
        super().__init__(
            master,
            option_var,
            *sorted(x['name'] for x in list(deck_positions.values())),
        )
        self.window = window
        self.option_var = option_var
        self.pack(anchor = tk.W, padx = 25, pady = (5, 10))