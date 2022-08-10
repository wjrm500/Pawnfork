import tkinter as tk
from logic.enums.Color import Color

from ui.abstract.BoardCanvas import BoardCanvas

class CreateOpeningBoardCanvas(BoardCanvas):
    def __init__(self, window: tk.Tk, master: tk.Frame, color: Color) -> None:
        super().__init__(window, master, color)
        self.has_moved = False
    
    def move_piece(self, from_square: str, to_square: str, castle_castling: bool = False) -> None:
        super().move_piece(from_square, to_square, castle_castling)
        if not self.has_moved: # If first move
            self.master.enable_save_button()
