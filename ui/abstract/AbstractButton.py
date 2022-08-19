import tkinter as tk

from ui.utils.ColorUtils import ColorUtils

class AbstractButton(tk.Button):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.original_background = self.cget('background')
        self.bind_events()
    
    def bind_events(self) -> None:
        self.bind('<Enter>', self.enter_handler)
        self.bind('<Leave>', self.leave_handler)
        self.bind('<Button-1>', self.click_handler)
    
    def enter_handler(self, event) -> None:
        self.window.configure(cursor = 'hand2')
        self.configure(background = ColorUtils.darken_hex(self.original_background, 0.1))
    
    def leave_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.configure(background = self.original_background)

    # @abstractmethod
    def click_handler(self, event) -> None:
        raise NotImplementedError
    
    def disable(self) -> None:
        self.configure(state = tk.DISABLED)
        self.unbind('<Enter>')
        self.unbind('<Leave>')
        self.unbind('<Button-1>')
    
    def enable(self) -> None:
        self.configure(state = tk.NORMAL)
        self.bind_events()