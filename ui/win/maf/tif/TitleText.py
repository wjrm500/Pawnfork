import tkinter as tk

from ui.ColorConsts import ColorConsts

class TitleText(tk.Text):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR,
            borderwidth = 0,
            height = 1,
            font = ('Cambria', 48),
        )
        self.window = window
        self.tag_configure('justify_center', justify = 'center')
        self.insert(tk.END, 'Pawnfork')
        self.tag_add('justify_center', '1.0', tk.END)
        self.config(state = tk.DISABLED)
        self.pack()