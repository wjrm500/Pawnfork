import tkinter as tk

from ui.abstract.AbsButton import AbsButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class TitleText(tk.Label, AbsButton):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.TITLE_FONT_FAMILY, 48),
        )
        self.window = window
        self.configure(text = 'Pawnfork')
        self.pack(anchor = tk.CENTER)
        AbsButton.__init__(self, darken_background = False)
    
    def click_handler(self, event) -> None:
        self.window.main_frame.set_frame_to_home()