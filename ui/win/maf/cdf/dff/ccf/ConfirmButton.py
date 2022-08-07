import tkinter as tk

from ui.abstract.AbsButton import AbsButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class ConfirmButton(tk.Button, AbsButton):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Confirm')
        self.pack(side = tk.LEFT, padx = (0, 5))
        AbsButton.__init__(self)
        
    def click_handler(self, event) -> None:
        self.master.master.handle_confirm(event)