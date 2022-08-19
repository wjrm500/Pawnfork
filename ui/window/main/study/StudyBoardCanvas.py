import tkinter as tk

from logic.enums.Color import Color
from ui.abstract.BoardCanvas import BoardCanvas

class StudyBoardCanvas(BoardCanvas):
    def __init__(self, window: tk.Tk, master: tk.Widget, color: Color) -> None:
        super().__init__(window, master, color)