import tkinter as tk

class SelectedOptionVar(tk.StringVar):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(master)
        self.window = window