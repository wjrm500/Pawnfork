import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class CreatingText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            foreground = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12, 'bold')
        )
        self.window = window
        self.configure(text = 'Creating...')
        self.configure(justify = tk.LEFT)
        self.pack()
        
    def pack(self):
        super().pack(anchor = tk.W, padx = 15, pady = 5)