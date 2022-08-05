import tkinter as tk

from ui.ColorConsts import ColorConsts
from ui.FontFamilyConsts import FontFamilyConsts

class CreateDeckButton(tk.Button):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Create a new deck')
        self.pack(fill = tk.X, padx = 25)