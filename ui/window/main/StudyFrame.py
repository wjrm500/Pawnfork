from playsound import playsound
import tkinter as tk
import winsound

from logic.board.Board import Board
from logic.enums.Color import Color
from logic.study.sqlalchemy.Deck import Deck
from ui.consts.ColorConsts import ColorConsts
from ui.window.main.study.StudyBoardCanvas import StudyBoardCanvas
from ui.window.main.study.NextFlashcardButton import NextFlashcardButton
from ui.window.main.study.UnderCanvasText import UnderCanvasText

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
        self.board = Board(self.flashcard)
        if self.canvas is not None:
            self.canvas.destroy()
        self.canvas = StudyBoardCanvas(self.window, self, self.deck.player_color)
        self.canvas.add_pieces(self.board.pieces)
        if self.under_canvas_text is not None:
            self.under_canvas_text.destroy()
        self.under_canvas_text = UnderCanvasText(self.window, self, self.flashcard)
        if self.next_flashcard_button is not None:
            self.next_flashcard_button.destroy()
        self.next_flashcard_button = NextFlashcardButton(self.window, self)
        self.next_flashcard_button.pack_forget()
    
    def move_piece(self, move: str) -> None:
        self.board.move_piece(move)
        correct = move == self.flashcard.best_move
        sound_filename = 'correct' if correct else 'incorrect'
        winsound.PlaySound(f'static\sounds\{sound_filename}.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
        text = 'Correct - you found the best move!' if correct else f'Incorrect - the best move is {self.flashcard.algebraic_best_move}.'
        self.under_canvas_text.configure(text = text)
        self.next_flashcard_button.pack()