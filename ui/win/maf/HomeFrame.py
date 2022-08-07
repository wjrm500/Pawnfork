import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.hof.DeckListOuterFrame import DeckListOuterFrame

class HomeFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.deck_list_frame = DeckListOuterFrame(self.window, self)
        self.pack(fill = tk.BOTH, expand = True)