import tkinter as tk

from logic.board.Board import Board
from logic.enums.Color import Color
from ui.consts.ColorConsts import ColorConsts
from ui.window.main.create_opening.CreateOpeningBoardCanvas import CreateOpeningBoardCanvas
from ui.window.main.create_opening.OpeningNameFrame import OpeningNameFrame
from ui.window.main.create_opening.SaveOpeningButton import SaveOpeningButton

class CreateOpeningFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.board = Board()
        self.canvas = CreateOpeningBoardCanvas(self.window, self, Color.WHITE)
        self.canvas.add_pieces(self.board.pieces)
        self.opening_name_frame = OpeningNameFrame(self.window, self)
        self.save_opening_button = SaveOpeningButton(self.window, self)
        self.pack(fill = tk.BOTH, expand = True)
    
    def move_piece(self, move: str) -> None:
        self.board.move_piece(move)
    
    def enable_save_button(self) -> None:
        self.save_opening_button.configure(state = tk.NORMAL)
    
    def handle_save(self) -> None:
        opening_name = self.opening_name_frame.opening_name_entry.get()
        self.window.database.persist_opening(opening_name, self.board.position)
        self.window.main_frame.set_frame_to_create_deck()