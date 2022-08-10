import math
import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class PostSubmitText(tk.Label):
    ERROR_DECK_EXISTS = 'A Deck with this exact configuration already exists!'
    ERROR_FIELD_REQUIRED = '{} is required'
    ERROR_NOT_NUMERIC = '{} must be numeric'
    ERROR_MAX_EXCEEDED = '{} cannot exceed {}'

    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12, 'bold')
        )
        self.window = window
        self.configure(text = 'Error')
        self.configure(justify = tk.LEFT)
        self.pack()
        
    def pack(self):
        super().pack(anchor = tk.W, padx = 15, pady = (5, 0))
    
    def show_estimated_flashcards(self, estimated_flashcards: int) -> None:
        self.configure(foreground = ColorConsts.BLACK)
        estimated_minutes_taken = math.ceil(estimated_flashcards / 3 / 60)
        add_s = '' if estimated_minutes_taken == 1 else 's'
        text = f'Up to {estimated_flashcards} flashcards may be created. This could take up to {estimated_minutes_taken} minute{add_s}.'
        self.configure(text = text)
        self.pack()
    
    def show_error(self, text: str) -> None:
        self.configure(foreground = ColorConsts.ERROR)
        self.configure(text = text)
        self.pack()