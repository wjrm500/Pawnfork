import tkinter as tk

from logic.board.pieces import *
from ui.win.MainFrame import MainFrame

class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Pawnfork')
        self.frame = MainFrame(self)
        self.dimension = 750
        self.center()
        
    def center(self):
        # From https://www.pythontutorial.net/tkinter/tkinter-window/

        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width / 2 - self.dimension / 2)
        center_y = int(screen_height / 2 - self.dimension / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f'{self.dimension}x{self.dimension}+{center_x}+{center_y}')

    def run(self) -> None:
        self.mainloop()