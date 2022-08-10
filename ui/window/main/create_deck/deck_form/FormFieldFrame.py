import tkinter as tk

from ui.consts.ColorConsts import ColorConsts

class FormFieldFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame, label: type, entry: type, option_var: type = None, *widgets) -> None:
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY,
            highlightthickness = 2,
            highlightbackground = ColorConsts.BLACK
        )
        self.window = window
        self.label = label(self.window, self)
        if option_var is not None:
            self.option_var = option_var(self.window, self)
            self.field = entry(self.window, self, self.option_var)
        else:
            self.field = entry(self.window, self)
        self.widgets = []
        for widget in widgets:
            self.widgets.append(widget(self.window, self))
        self.pack(fill = tk.X, padx = 15, pady = (15, 0))