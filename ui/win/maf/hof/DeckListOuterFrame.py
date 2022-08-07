import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.hof.DeckListInnerFrame import DeckListInnerFrame

class DeckListOuterFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.deck_list_frame = DeckListInnerFrame(self.window, self)
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))
    
    def on_mousewheel(self, event) -> None:
        self.canvas.yview_scroll(-1 * (event.delta // 120), 'units')