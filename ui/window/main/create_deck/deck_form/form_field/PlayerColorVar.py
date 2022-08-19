import tkinter as tk

class PlayerColorVar(tk.StringVar):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(master)
        self.window = window