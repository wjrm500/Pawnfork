import tkinter as tk

from ui.abstract.AbstractButton import AbstractButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class TitleText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            borderwidth = 0,
            height = 1,
            font = (FontFamilyConsts.TITLE_FONT_FAMILY, 40),
        )
        self.window = window
        self.configure(text = 'Pawnfork')
        self.pack(anchor = tk.CENTER)
        self.bind('<Enter>', self.enter_handler)
        self.bind('<Leave>', self.leave_handler)
        self.bind('<Button-1>', self.click_handler)

    def enter_handler(self, event) -> None:
        self.window.configure(cursor = 'hand2')
    
    def leave_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
    
    def click_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.window.main_frame.set_frame_to_home()