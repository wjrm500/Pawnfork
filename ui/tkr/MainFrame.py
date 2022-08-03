import tkinter as tk

from ui.tkr.maf.BoardCanvasFrame import BoardCanvasFrame
from ui.tkr.maf.HomeFrame import HomeFrame
from ui.tkr.maf.TitleFrame import TitleFrame

class MainFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.title_frame = TitleFrame(self)
        self.set_frame_to_board_canvas()
        self.pack(fill = tk.BOTH, expand = True)
    
    def set_frame_to_home(self) -> None:
        self.frame = HomeFrame(self)
    
    def set_frame_to_board_canvas(self) -> None:
        self.frame = BoardCanvasFrame(self)