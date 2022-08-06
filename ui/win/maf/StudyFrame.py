import tkinter as tk

from logic.board.Board import Board
from logic.study.sqlalchemy.Deck import Deck
from logic.study.sqlalchemy.Flashcard import Flashcard
from ui.ColorConsts import ColorConsts
from ui.win.maf.stf.BoardCanvas import BoardCanvas
from ui.win.maf.stf.NextFlashcardButton import NextFlashcardButton
from ui.win.maf.stf.UnderCanvasText import UnderCanvasText

class StudyFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk, deck: Deck) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.deck = deck
        self.canvas = None
        self.under_canvas_text = None
        self.next_flashcard_button = None
        self.load_new_flashcard()
        self.pack(fill = tk.BOTH, expand = True)
    
    def load_new_flashcard(self) -> None:
        self.flashcard = self.deck.get_random_flashcard()
        self.board = Board(self.flashcard.position)
        if self.canvas is not None:
            self.canvas.destroy()
        self.canvas = BoardCanvas(self.window, self)
        self.canvas.add_pieces(self.board.pieces)
        if self.under_canvas_text is not None:
            self.under_canvas_text.destroy()
        self.under_canvas_text = UnderCanvasText(self.window, self, self.flashcard)
        if self.next_flashcard_button is not None:
            self.next_flashcard_button.destroy()
        self.next_flashcard_button = NextFlashcardButton(self.window, self)
        self.next_flashcard_button.pack_forget()
    
    def move_piece(self, move: str) -> None:
        best_move = self.board.move_piece(move)
        text = 'Correct - you found the best move!' if move == best_move else f'Incorrect - the best move is {best_move}.'
        self.under_canvas_text.configure(text = text)
        self.next_flashcard_button.pack(fill = tk.X, padx = 25)