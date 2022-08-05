import tkinter as tk

from ui.ColorConsts import ColorConsts

class CreateDeckButton(tk.Button):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.LIME_GREEN,
            font = ('Cambria', 14),
            relief = tk.FLAT,
            borderwidth = 0
        )
        self.window = window
        self.configure(text = 'Create a new deck')
        self.pack()