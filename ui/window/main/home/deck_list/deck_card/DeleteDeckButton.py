import tkinter as tk
from logic.study.sqlalchemy.Deck import Deck

from ui.abstract.AbstractButton import AbstractButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class DeleteDeckButton(AbstractButton):
    def __init__(self, window: tk.Tk, master: tk.Frame, deck: Deck) -> None:
        super().__init__(
            master,
            foreground = ColorConsts.WHITE,
            background = ColorConsts.ERROR,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 10, 'bold'),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.deck = deck
        self.configure(text = '✕')
        self.pack(side = tk.RIGHT, anchor = tk.N, padx = 5, pady = 5)
    
    def click_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.window.database.delete_deck(self.deck)
        self.window.main_frame.set_frame_to_home()