import tkinter as tk

from logic.consts.deck_positions import deck_positions
from ui.consts.ColorConsts import ColorConsts
from ui.consts.FontFamilyConsts import FontFamilyConsts
from ui.win.maf.cdf.dff.fff.ope.SelectedOptionVar import SelectedOptionVar

class OpeningEntry(tk.OptionMenu):
    def __init__(self, window: tk.Tk, master: tk.Frame, option_var: tk.StringVar):
        super().__init__(
            master,
            option_var,
            *['Italian Game', 'Ruy Lopez Opening'],
            # background = ColorConsts.LIGHT_GREY,
            # borderwidth = 0,
            # height = 1,
            # font = (FontFamilyConsts.MAIN_FONT_FAMILY, 12)
        )
        self.window = window
        self.option_var = option_var
        # self.configure(variable = SelectedOptionVar(self))
        # self.configure(options = ['Italian Game', 'Ruy Lopez Opening'])
        
        self.pack(anchor = tk.W, padx = 25, pady = (5, 10))