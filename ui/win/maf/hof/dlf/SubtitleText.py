import tkinter as tk

from ui.ColorConsts import ColorConsts
from ui.FontFamilyConsts import FontFamilyConsts

class SubtitleText(tk.Text):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 16),
        )
        self.window = window
        self.tag_configure('justify_center', justify = 'center')
        self.insert(tk.END, 'Click a deck to study!')
        self.config(state = tk.DISABLED)
        self.pack(padx = 25, pady = (25, 0))