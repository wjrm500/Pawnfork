import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.window.main.create_deck.DeckFormFrame import DeckFormFrame

class CreateDeckFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.deck_list_frame = DeckFormFrame(self.window, self)
        self.pack(fill = tk.BOTH, expand = True)