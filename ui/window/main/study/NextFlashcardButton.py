import tkinter as tk

from ui.abstract.AbstractButton import AbstractButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class NextFlashcardButton(AbstractButton):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Next flashcard')
        self.pack()

    def click_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.master.load_new_flashcard()
    
    def pack(self) -> None:
        super().pack(padx = 15)