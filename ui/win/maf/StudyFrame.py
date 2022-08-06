import tkinter as tk

from logic.board.Board import Board
from logic.study.sqlalchemy.Deck import Deck
from ui.ColorConsts import ColorConsts
from ui.win.maf.stf.BoardCanvas import BoardCanvas

class StudyFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk, deck: Deck) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.deck = deck

        self.board = Board()
        for move in deck.start_position.moves:
            self.board.get_square(move.from_square()).piece.move(self.board.get_square(move.to_square()))
        
        self.canvas = BoardCanvas(self.window, self)
        self.canvas.add_pieces(self.board.pieces)

        self.pack(fill = tk.BOTH, expand = True)