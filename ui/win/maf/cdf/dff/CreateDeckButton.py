import tkinter as tk
from typing import List, Literal

from ui.abstract.AbsButton import AbsButton
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts

class CreateDeckButton(tk.Button, AbsButton):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.GREEN,
            font = (FontFamilyConsts.MAIN_FONT_FAMILY, 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Create')
        self.pack(anchor = tk.W, padx = 25, pady = (25, 0))
        AbsButton.__init__(self)
        
    def click_handler(self, event) -> None:
        opening = self.master.opening_field_frame.field.option_var.get()
        turn_depth = self.master.turn_depth_field_frame.field.get()
        response_depth = self.master.response_depth_field_frame.field.get()
        error_messages = []
        error_messages = self.validate_opening(error_messages, opening)
        error_messages = self.validate_depth(error_messages, turn_depth, 'Turn')
        error_messages = self.validate_depth(error_messages, response_depth, 'Response')
        if len(error_messages):
            error_message = '\n'.join(error_messages)
            self.master.show_error(error_message)
        else:
            pass
    
    def validate_opening(self, error_messages: List[str], opening: str) -> str:
        if opening == '':
            error_messages.append('Opening is required')
        return error_messages
    
    def validate_depth(self, error_messages: List[str], depth: int, type: Literal['Turn', 'Response']) -> None:
        if depth == '':
            return error_messages + [f'{type} depth is required']
        if not depth.isnumeric():
            return error_messages + [f'{type} depth must be numeric']
        max_depth = 10
        if int(depth) > max_depth:
            return error_messages + [f'{type} depth cannot exceed {max_depth}']
        return error_messages