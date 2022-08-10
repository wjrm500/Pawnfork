import tkinter as tk
from typing import List

from logic.study.sqlalchemy.Opening import Opening

class OpeningEntry(tk.OptionMenu):
    def __init__(self, window: tk.Tk, master: tk.Frame, option_var: tk.StringVar) -> None:
        super().__init__(
            master,
            option_var,
            'PLACEHOLDER'
        )
        self.window = window
        self.option_var = option_var
        menu = self['menu']
        menu.delete(0, tk.END)
        for opening in self.window.database.get_openings():
            menu.add_command(label = opening.name, command = tk._setit(self.option_var, opening.name))
        self.pack(anchor = tk.W, padx = 15, pady = (5, 10))