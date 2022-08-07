import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.hof.dlf.CreateDeckButton import CreateDeckButton
from ui.win.maf.hof.dlf.DeckCardFrame import DeckCardFrame
from ui.win.maf.hof.dlf.SubtitleText import SubtitleText

class DeckListFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.subtitle_text = SubtitleText(self.window, self)
        self.deck_card_frames = []
        for deck in self.window.database.get_decks():
            self.deck_card_frames.append(DeckCardFrame(self.window, self, deck))
        self.create_deck_button = CreateDeckButton(self.window, self)
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))