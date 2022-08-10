import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.window.main.create_deck.deck_form.form_field.CreateOpeningButton import CreateOpeningButton
from ui.window.main.create_deck.deck_form.form_field.OpeningLabel import OpeningLabel

class FormFieldFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame, label: type, entry: type, option_var: type = None) -> None:
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY
        )
        self.window = window
        self.label = label(self.window, self)
        if option_var is not None:
            self.option_var = option_var(self.window, self)
            self.field = entry(self.window, self, self.option_var)
        else:
            self.field = entry(self.window, self)
        if label == OpeningLabel:
            CreateOpeningButton(self.window, self)
        self.pack(fill = tk.X, padx = 25, pady = (15, 0))