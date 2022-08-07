import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.hof.DeckListFrame import DeckListFrame

class HomeFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.deck_list_frame = DeckListFrame(self.window, self)
        self.pack(fill = tk.BOTH, expand = True)