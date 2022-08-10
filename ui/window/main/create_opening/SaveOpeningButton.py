import tkinter as tk

from ui.abstract.AbsButton import AbsButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class SaveOpeningButton(tk.Button, AbsButton):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Save')
        self.configure(state = tk.DISABLED)
        self.pack()
        AbsButton.__init__(self)

    def click_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.master.save_opening()
    
    def pack(self) -> None:
        super().pack(padx = 25)