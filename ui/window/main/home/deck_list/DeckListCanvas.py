import tkinter as tk
from tkinter import ttk

from ui.consts.ColorConsts import ColorConsts

class DeckListCanvas(tk.Canvas):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            bd = 0,
            highlightthickness = 0,
            background = ColorConsts.WHITE
        )
        self.window = window
        self.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    
    def put_frame_in_window(self, canvas_frame: tk.Frame, scrollbar: ttk.Scrollbar) -> None:
        self.canvas_frame = self.create_window((0, 0), window = canvas_frame, anchor = tk.NW, width = self.window.dimension - 60)
        self.configure(yscrollcommand = scrollbar.set)