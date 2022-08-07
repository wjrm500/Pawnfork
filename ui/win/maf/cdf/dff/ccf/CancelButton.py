import tkinter as tk

from ui.abstract.AbsButton import AbsButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class CancelButton(tk.Button, AbsButton):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.ERROR,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Cancel')
        self.pack(side = tk.RIGHT, padx = (5, 0))
        AbsButton.__init__(self)
        
    def click_handler(self, event) -> None:
        pass