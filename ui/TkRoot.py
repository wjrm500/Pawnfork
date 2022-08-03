import tkinter as tk

from logic.pieces import *
from ui.tkr.MainFrame import MainFrame

class TkRoot(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Pawnfork')
        self.frame = MainFrame(self)
        
    def run(self) -> None:
        self.mainloop()