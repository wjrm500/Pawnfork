import tkinter as tk

from ui.abstract.AbstractButton import AbstractButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class SaveOpeningButton(AbstractButton):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Save')
        self.pack()
        self.disable()

    def click_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.master.handle_save()