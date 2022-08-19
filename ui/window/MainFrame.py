import tkinter as tk
from logic.study.sqlalchemy.Deck import Deck
from ui.window.main.CreateDeckFrame import CreateDeckFrame
from ui.window.main.CreateOpeningFrame import CreateOpeningFrame

from ui.window.main.StudyFrame import StudyFrame
from ui.window.main.HomeFrame import HomeFrame
from ui.window.main.TitleFrame import TitleFrame

class MainFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Widget) -> None:
        super().__init__(master)
        self.window = window
        self.title_frame = TitleFrame(self.window, self)
        self.frame = None
        self.set_frame_to_home()
        self.pack(fill = tk.BOTH, expand = True)
    
    def set_frame_to_home(self) -> None:
        if self.frame is not None:
            self.frame.destroy()
        self.frame = HomeFrame(self.window, self)
    
    def set_frame_to_study(self, deck: Deck) -> None:
        if self.frame is not None:
            self.frame.destroy()
        self.frame = StudyFrame(self.window, self, deck)
    
    def set_frame_to_create_deck(self) -> None:
        if self.frame is not None:
            self.frame.destroy()
        self.frame = CreateDeckFrame(self.window, self)
    
    def set_frame_to_create_opening(self) -> None:
        if self.frame is not None:
            self.frame.destroy()
        self.frame = CreateOpeningFrame(self.window, self)