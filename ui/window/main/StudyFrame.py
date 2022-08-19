import tkinter as tk
from typing import Callable, Tuple
import winsound

from logic.board.Board import Board
from logic.study.sqlalchemy.Deck import Deck
from ui.consts.ColorConsts import ColorConsts
from ui.window.main.study.PreviousMovesText import PreviousMovesText
from ui.window.main.study.StudyBoardCanvas import StudyBoardCanvas
from ui.window.main.study.NextFlashcardButton import NextFlashcardButton
from ui.window.main.study.PromptUserText import PromptUserText

class StudyFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Widget, deck: Deck) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.deck = deck
        self.canvas = None
        self.previous_moves_text = None
        self.prompt_user_text = None
        self.next_flashcard_button = None
        self.load_new_flashcard()
        self.pack(fill = tk.BOTH, expand = True)
    
    def create_widget(self, widget_name: str, widget: tk.Widget, widget_args: Tuple, widget_callback: Callable = None) -> None:
        if (bound_widget := getattr(self, widget_name)) is not None:
            bound_widget.destroy()
        setattr(self, widget_name, widget(*widget_args))
        if widget_callback:
            widget_callback(getattr(self, widget_name))

    def load_new_flashcard(self) -> None:
        self.flashcard = self.deck.get_random_flashcard()
        self.board = Board(self.flashcard)
        self.create_widget('canvas', StudyBoardCanvas, (self.window, self, self.deck.player_color), lambda w: w.add_pieces(self.board.pieces))
        self.create_widget('previous_moves_text', PreviousMovesText, (self.window, self, self.flashcard))
        self.create_widget('prompt_user_text', PromptUserText, (self.window, self, self.flashcard))
        self.create_widget('next_flashcard_button', NextFlashcardButton, (self.window, self), lambda w: w.pack_forget())
    
    def move_piece(self, move: str) -> None:
        self.board.move_piece(move)
        correct = move == self.flashcard.best_move
        sound_filename = 'correct' if correct else 'incorrect'
        winsound.PlaySound(f'static\sounds\{sound_filename}.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
        text = 'Correct - you found the best move!' if correct else f'Incorrect - the best move is {self.flashcard.algebraic_best_move}.'
        self.prompt_user_text.configure(text = text)
        self.next_flashcard_button.pack()