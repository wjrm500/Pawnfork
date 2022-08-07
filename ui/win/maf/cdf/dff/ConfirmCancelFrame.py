import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.cdf.dff.ccf.CancelButton import CancelButton
from ui.win.maf.cdf.dff.ccf.ConfirmButton import ConfirmButton

class ConfirmCancelFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE
        )
        self.window = window
        self.confirm_button = ConfirmButton(self.window, self)
        self.cancel_button = CancelButton(self.window, self)
        self.pack()
    
    def pack(self) -> None:
        super().pack(anchor = tk.W, padx = 25, pady = (10, 0))