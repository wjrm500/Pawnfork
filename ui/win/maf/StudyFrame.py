import tkinter as tk

from logic.board.Board import Board
from logic.study.sqlalchemy.Deck import Deck
from logic.study.sqlalchemy.Flashcard import Flashcard
from ui.ColorConsts import ColorConsts
from ui.win.maf.stf.BoardCanvas import BoardCanvas
from ui.win.maf.stf.UnderCanvasText import UnderCanvasText

class StudyFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk, deck: Deck) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.deck = deck
        self.flashcard = self.deck.get_random_flashcard()
        self.board = Board(self.flashcard.position)
        self.canvas = BoardCanvas(self.window, self)
        self.canvas.add_pieces(self.board.pieces)
        self.under_canvas_text = UnderCanvasText(self.window, self, self.flashcard)
        self.pack(fill = tk.BOTH, expand = True)
    
    def move(self, move: str) -> None:
        best_move = self.board.move(move)
        text = 'Correct - you found the best move!' if move == best_move else f'Incorrect - the best move is {best_move}.'
        self.under_canvas_text.configure(text = text)