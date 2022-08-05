import tkinter as tk

class CreateDeckButton(tk.Button):
    def __init__(self, master: tk.Frame):
        super().__init__(master)
        self.pack()