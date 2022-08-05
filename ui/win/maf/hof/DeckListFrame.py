import tkinter as tk

from ui.ColorConsts import ColorConsts
from ui.win.maf.hof.dlf.CreateDeckButton import CreateDeckButton
from ui.win.maf.hof.dlf.DeckCardFrame import DeckCardFrame
from ui.win.maf.hof.dlf.SubtitleText import SubtitleText

class DeckListFrame(tk.Frame):
    def __init__(self, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.subtitle_text = SubtitleText(self)
        self.deck_card_frames = []
        for _ in range(5):
            self.deck_card_frames.append(DeckCardFrame(self))
        self.create_deck_button = CreateDeckButton(self)
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = 20)