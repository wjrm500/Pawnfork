import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.window.main.home.deck_list.CreateDeckButton import CreateDeckButton
from ui.window.main.home.deck_list.DeckCardFrame import DeckCardFrame
from ui.window.main.home.deck_list.DeckListCanvas import DeckListCanvas
from ui.window.main.home.deck_list.DeckListCanvasFrame import DeckListCanvasFrame
from ui.window.main.home.deck_list.DeckListScrollbar import DeckListScrollbar
from ui.window.main.home.deck_list.SubtitleText import SubtitleText

class DeckListFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.inner_frame = tk.Frame(self) # Need inner frame as canvas overlaps border of outer frame otherwise
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))
        self.canvas = DeckListCanvas(self.window, self.inner_frame)
        self.scrollbar = DeckListScrollbar(self.window, self.inner_frame, self.canvas)
        self.canvas_frame = DeckListCanvasFrame(self.window, self.inner_frame, self.canvas)
        self.canvas.put_frame_in_window(self.canvas_frame, self.scrollbar)
        self.subtitle_text = SubtitleText(self.window, self.canvas_frame)
        self.deck_card_frames = []
        for deck in self.window.database.get_decks():
            self.deck_card_frames.append(DeckCardFrame(self.window, self.canvas_frame, deck))
        self.create_deck_button = CreateDeckButton(self.window, self.canvas_frame)
        self.inner_frame.pack(fill = tk.BOTH, expand = True)
        for widget in (self.canvas_frame, self.subtitle_text, self.create_deck_button, *self.deck_card_frames):
            widget.bind('<MouseWheel>', self.on_mousewheel)
    
    def on_mousewheel(self, event) -> None:
        self.canvas.yview_scroll(-1 * (event.delta // 120), 'units')