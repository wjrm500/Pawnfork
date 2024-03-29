import tkinter as tk

from logic.study.sqlalchemy.Deck import Deck
from ui.consts.ColorConsts import ColorConsts
from ui.window.main.home.deck_list.deck_card.DeckInfoFrame import DeckInfoFrame
from ui.window.main.home.deck_list.deck_card.DeleteDeckButton import DeleteDeckButton

class DeckCardFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Widget, deck: Deck) -> None:
        super().__init__(
            master,
            background = ColorConsts.LIGHT_GREY,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.deck = deck
        self.deck_info_frame = DeckInfoFrame(self.window, self, self.deck)
        self.delete_deck_button = DeleteDeckButton(self.window, self, self.deck)
        self.pack(fill = tk.X, padx = 15, pady = (15, 0))
        self.sub_widgets = [self, self.deck_info_frame, self.deck_info_frame.deck_name_text, self.deck_info_frame.deck_data_text]
        self.add_hover_event()
        self.add_click_event()
    
    def add_hover_event(self) -> None:
        self.bind('<Enter>', self.enter_handler)
        self.bind('<Leave>', self.leave_handler)
    
    def add_click_event(self) -> None:
        for widget in self.sub_widgets:
            widget.bind('<Button-1>', self.click_handler)
    
    def enter_handler(self, event) -> None:
        self.window.configure(cursor = 'hand2')
        for widget in self.sub_widgets:
            widget.configure(background = ColorConsts.MEDIUM_GREY)
    
    def leave_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        for widget in self.sub_widgets:
            widget.configure(background = ColorConsts.LIGHT_GREY)
    
    def click_handler(self, event) -> None:
        self.window.configure(cursor = 'arrow')
        self.window.main_frame.set_frame_to_study(self.deck)