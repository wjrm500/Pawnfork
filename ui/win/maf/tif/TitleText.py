import tkinter as tk

from ui.ColorConsts import ColorConsts
from ui.FontFamilyConsts import FontFamilyConsts

class TitleText(tk.Text):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.TITLE_FONT_FAMILY, 48),
        )
        self.window = window
        self.tag_configure('justify_center', justify = 'center')
        self.insert(tk.END, 'Pawnfork')
        self.tag_add('justify_center', '1.0', tk.END)
        self.config(state = tk.DISABLED)
        self.pack()