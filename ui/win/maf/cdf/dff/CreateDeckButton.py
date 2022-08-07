import tkinter as tk
from typing import List, Literal

from ui.abstract.AbsButton import AbsButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class CreateDeckButton(tk.Button, AbsButton):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Create')
        self.pack(anchor = tk.W, padx = 25, pady = (25, 0))
        AbsButton.__init__(self)
        
    def click_handler(self, event) -> None:
        self.master.handle_create(event)