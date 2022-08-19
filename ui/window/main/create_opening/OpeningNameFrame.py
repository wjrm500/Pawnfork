import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.window.main.create_opening.opening_name.OpeningNameEntry import OpeningNameEntry
from ui.window.main.create_opening.opening_name.OpeningNameLabel import OpeningNameLabel

class OpeningNameFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.opening_name_label = OpeningNameLabel(self.window, self)
        self.opening_name_entry = OpeningNameEntry(self.window, self)
        self.pack()