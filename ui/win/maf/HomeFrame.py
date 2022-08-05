import tkinter as tk

from ui.ColorConsts import ColorConsts
from ui.win.maf.hof.DeckListFrame import DeckListFrame

class HomeFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR
        )
        self.deck_list_frame = DeckListFrame(self)
        self.pack(fill = tk.BOTH, expand = True)