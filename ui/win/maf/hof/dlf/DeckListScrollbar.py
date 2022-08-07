import tkinter as tk
from tkinter import ttk

from ui.consts.ColorConsts import ColorConsts

class DeckListScrollbar(ttk.Scrollbar):
    def __init__(self, window: tk.Tk, master: tk.Frame, canvas: tk.Canvas) -> None:
        super().__init__(
            master,
            orient = tk.VERTICAL,
            command = canvas.yview
        )
        self.window = window
        self.pack(side = tk.RIGHT, fill = tk.Y)