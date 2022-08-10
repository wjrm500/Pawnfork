import tkinter as tk

from logic.board.Board import Board
from logic.enums.Color import Color
from logic.study.sqlalchemy.Deck import Deck
from ui.consts.ColorConsts import ColorConsts
from ui.window.main.study.BoardCanvas import BoardCanvas

class CreateOpeningFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.board = Board()
        self.canvas = BoardCanvas(self.window, self, Color.WHITE)
        self.canvas.add_pieces(self.board.pieces)
        self.pack(fill = tk.BOTH, expand = True)
    
    def move_piece(self, move: str) -> None:
        self.board.move_piece(move)