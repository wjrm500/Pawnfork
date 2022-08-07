import tkinter as tk

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
        if opening == '':
            error_messages.append('Opening is required')
        if turn_depth == '':
            error_messages.append('Turn depth is required')
        if response_depth == '':
            error_messages.append('Response depth is required')
        if len(error_messages):
            error_message = '\n'.join(error_messages)
            self.master.show_error(error_message)
        else:
            pass