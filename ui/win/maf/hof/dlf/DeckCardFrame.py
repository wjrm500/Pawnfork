import tkinter as tk

from logic.study.sqlalchemy.Deck import Deck
from ui.ColorConsts import ColorConsts
from ui.win.maf.hof.dlf.dcf.DeckDataText import DeckDataText
from ui.win.maf.hof.dlf.dcf.DeckNameText import DeckNameText

class DeckCardFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame, deck: Deck):
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.deck = deck
        self.deck_name_text = DeckNameText(self.window, self, self.deck)
        self.deck_data_text = DeckDataText(self.window, self, self.deck)
        self.pack(padx = 25, pady = 25)