import tkinter as tk

from ui.win.maf.StudyFrame import StudyFrame
from ui.win.maf.HomeFrame import HomeFrame
from ui.win.maf.TitleFrame import TitleFrame

class MainFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Tk) -> None:
        super().__init__(master)
        self.window = window
        self.title_frame = TitleFrame(self.window, self)
        self.set_frame_to_home()
        self.pack(fill = tk.BOTH, expand = True)
    
    def set_frame_to_home(self) -> None:
        self.frame = HomeFrame(self.window, self)
    
    def set_frame_to_study(self) -> None:
        self.frame = StudyFrame(self.window, self)