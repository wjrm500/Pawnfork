import tkinter as tk
from logic.study.sqlalchemy.Deck import Deck

from ui.win.maf.StudyFrame import StudyFrame
from ui.win.maf.HomeFrame import HomeFrame
from ui.win.maf.TitleFrame import TitleFrame

class MainFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(master)
        self.window = window
        self.title_frame = TitleFrame(self.window, self)
        self.frame = None
        self.set_frame_to_home()
        # self.set_frame_to_study(self.window.database.get_decks()[0])
        self.pack(fill = tk.BOTH, expand = True)
    
    def set_frame_to_home(self) -> None:
        if self.frame is not None:
            self.frame.destroy()
        self.frame = HomeFrame(self.window, self)
    
    def set_frame_to_study(self, deck: Deck) -> None:
        if self.frame is not None:
            self.frame.destroy()
        self.frame = StudyFrame(self.window, self, deck)