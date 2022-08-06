import tkinter as tk
from logic.board.Board import Board

from ui.ColorConsts import ColorConsts
from ui.FontFamilyConsts import FontFamilyConsts

class NextFlashcardButton(tk.Button):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Next flashcard')
        self.pack(fill = tk.X, padx = 25)
        self.bind('<Button-1>', self.click_handler)

    def click_handler(self, event) -> None:
        self.master.load_new_flashcard()