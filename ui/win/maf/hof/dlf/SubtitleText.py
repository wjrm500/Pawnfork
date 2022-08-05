import tkinter as tk

from ui.ColorConsts import ColorConsts

class SubtitleText(tk.Text):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR,
            borderwidth = 0,
            height = 1,
            font = ('Cambria', 16),
        )
        self.window = window
        self.tag_configure('justify_center', justify = 'center')
        self.insert(tk.END, 'Click a deck to study!')
        self.config(state = tk.DISABLED)
        self.pack()