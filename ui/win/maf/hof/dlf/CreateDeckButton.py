import tkinter as tk

class CreateDeckButton(tk.Button):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(master)
        self.window = window
        self.pack()