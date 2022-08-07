import tkinter as tk
from logic.study.sqlalchemy.Flashcard import Flashcard

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class UnderCanvasText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Frame, flashcard: Flashcard) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14)
        )
        self.window = window
        self.flashcard = flashcard
        opponents_move = self.flashcard.opponents_move().definition
        self.configure(text = f'Your opponent played {opponents_move}. Make your move!')
        self.pack(anchor = tk.CENTER, padx = 10, pady = (10, 5))