import tkinter as tk

from ui.consts.ColorConsts import ColorConsts

class DeckListCanvasFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Widget, canvas: tk.Canvas) -> None:
        super().__init__(
            master,
            background = ColorConsts.WHITE
        )
        self.window = window
        self.canvas = canvas
        self.bind('<Configure>', self.on_configure)
    
    def on_configure(self, event) -> None:
        # Courtesy of https://stackoverflow.com/questions/60711834/canvas-scrolling-up-when-it-shouldnt
        bbox = self.canvas.bbox('all')
        x, y, width, height = bbox
        if height < self.canvas.winfo_height():
            bbox = x, y, width, self.canvas.winfo_height()
        self.canvas.configure(scrollregion = bbox)