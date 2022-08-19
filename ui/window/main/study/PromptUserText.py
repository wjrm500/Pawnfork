import tkinter as tk
from logic.study.sqlalchemy.Flashcard import Flashcard

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class PromptUserText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Widget, flashcard: Flashcard) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            height = 1,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14)
        )
        self.window = window
        self.flashcard = flashcard
        self.configure(text = f'Your opponent played {self.flashcard.algebraic_opponents_move}. Make your move!')
        self.pack(anchor = tk.CENTER, padx = 10, pady = 5)