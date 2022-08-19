import tkinter as tk

from logic.study.sqlalchemy.Flashcard import Flashcard
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class PreviousMovesText(tk.Label):
    def __init__(self, window: tk.Tk, master: tk.Widget, flashcard: Flashcard) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 10, 'italic'),
            wraplength = 500
        )
        self.window = window
        self.flashcard = flashcard
        previous_moves_text = ', '.join(move.definition for move in flashcard.moves)
        self.configure(text = f'Previous moves: {previous_moves_text}')
        self.pack(anchor = tk.CENTER, padx = 10, pady = (10, 5))