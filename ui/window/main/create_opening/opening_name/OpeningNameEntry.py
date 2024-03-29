import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class OpeningNameEntry(tk.Entry):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12)
        )
        self.window = window
        self.pack(side = tk.RIGHT, padx = (5, 10), pady = 10)
        self.bind('<KeyRelease>', self.handle_key_release)
    
    def handle_key_release(self, event) -> None:
        entry_empty = self.get() == ''
        self.master.master.handle_name_key_release(entry_empty)