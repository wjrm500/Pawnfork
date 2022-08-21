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
        flashcard_turns = [flashcard.moves[i:i + 2] for i in range(0, len(flashcard.moves), 2)]
        turn_texts = []
        for i, turn in enumerate(flashcard_turns, 1):
            text = f'{i}. {turn[0].algebraic_definition}'
            if len(turn) > 1:
                text += f' {turn[1].algebraic_definition}'
            turn_texts.append(text)
        previous_moves_text = ', '.join(turn_texts)
        self.configure(text = f'Previous moves: {previous_moves_text}')
        self.pack(anchor = tk.CENTER, padx = 10, pady = (10, 5))