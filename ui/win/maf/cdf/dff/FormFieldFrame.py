import tkinter as tk

from ui.consts.ColorConsts import ColorConsts

class FormFieldFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame, label: type, entry: type):
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY
        )
        self.window = window
        self.label = label(self.window, self)
        self.field = entry(self.window, self)
        self.pack(fill = tk.X, padx = 25, pady = (25, 0))