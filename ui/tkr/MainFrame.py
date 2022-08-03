import tkinter

from ui.tkr.maf.BoardCanvasFrame import BoardCanvasFrame
from ui.tkr.maf.HomeFrame import HomeFrame

class MainFrame(tkinter.Frame):
    def __init__(self, master: tkinter.Tk) -> None:
        super().__init__(master)
        self.set_frame_to_board_canvas()
        self.pack(fill = tkinter.BOTH, expand = True)
    
    def set_frame_to_home(self) -> None:
        self.frame = HomeFrame(self)
    
    def set_frame_to_board_canvas(self) -> None:
        self.frame = BoardCanvasFrame(self)