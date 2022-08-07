from abc import ABC, abstractmethod

from ui.utils.ColorUtils import ColorUtils

class AbsButton(ABC):
    def __init__(self, darken_background: bool = True) -> None:
        self.darken_background = darken_background
        self.original_background = self.cget('background')
        self.bind('<Enter>', self.enter_handler)
        self.bind('<Leave>', self.leave_handler)
        self.bind('<Button-1>', self.click_handler)
    
    def enter_handler(self, event) -> None:
        self.window.configure(cursor = 'hand2')
        if self.darken_background:
            self.configure(background = ColorUtils.darken_hex(self.original_background, 0.1))
    
    def leave_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.configure(background = self.original_background)

    @abstractmethod
    def click_handler(self, event) -> None:
        raise NotImplementedError