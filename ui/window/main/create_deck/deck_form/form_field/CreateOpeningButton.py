import tkinter as tk

from ui.abstract.AbstractButton import AbstractButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class CreateOpeningButton(AbstractButton):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Create new opening')
        self.pack(anchor = tk.W, padx = 15, pady = (0, 10))
        
    def click_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.window.main_frame.set_frame_to_create_opening()