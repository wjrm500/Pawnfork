import tkinter as tk

from logic.board.Board import Board
from logic.enums.Color import Color
from ui.consts.ColorConsts import ColorConsts
from ui.window.main.create_opening.CreateOpeningBoardCanvas import CreateOpeningBoardCanvas
from ui.window.main.create_opening.OpeningNameFrame import OpeningNameFrame
from ui.window.main.create_opening.SaveErrorText import SaveErrorText
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
        self.save_error_text = SaveErrorText(self.window, self)
        self.pack(fill = tk.BOTH, expand = True)
    
    def move_piece(self, move: str) -> None:
        self.board.move_piece(move)
    
    def handle_first_move(self) -> None:
        if self.opening_name_frame.opening_name_entry.get() != '':
            self.enable_save_button()
        
    def handle_name_key_release(self, entry_empty: bool) -> None:
        if entry_empty:
            self.disable_save_button()
        else:
            if self.canvas.has_moved:
                self.enable_save_button()
            
        
    def enable_save_button(self) -> None:
        self.save_opening_button.enable()
    
    def disable_save_button(self) -> None:
        self.save_opening_button.disable()
    
    def handle_save(self) -> None:
        opening_name = self.opening_name_frame.opening_name_entry.get()
        saved = self.window.database.persist_opening(opening_name, self.board.position)
        if saved:
            self.window.main_frame.set_frame_to_create_deck()
        else:
            self.save_error_text.pack()