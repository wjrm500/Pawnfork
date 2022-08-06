import tkinter as tk

from logic.board.pieces import *
from logic.study.sqlalchemy.Database import Database
from ui.win.MainFrame import MainFrame

class Window(tk.Tk):
    main_frame: MainFrame

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.database = database
        self.title('Pawnfork')
        self.main_frame = MainFrame(self, self)
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