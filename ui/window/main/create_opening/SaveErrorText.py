import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class SaveErrorText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            foreground = ColorConsts.ERROR,
            background = ColorConsts.MEDIUM_GREY,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12, 'bold')
        )
        self.window = window
        self.configure(text = 'Opening name has already been used!')
    
    def pack(self) -> None:
        super().pack(pady = 10)