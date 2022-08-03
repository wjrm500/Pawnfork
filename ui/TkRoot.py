import tkinter

from logic.pieces import *
from ui.MainFrame import MainFrame

class TkRoot(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Pawnfork')
        self.frame = MainFrame(self)
        
    def run(self) -> None:
        self.mainloop()