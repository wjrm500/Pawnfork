import tkinter as tk
from tkinter import ttk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.hof.dlf.CreateDeckButton import CreateDeckButton
from ui.win.maf.hof.dlf.DeckCardFrame import DeckCardFrame
from ui.win.maf.hof.dlf.DeckListCanvas import DeckListCanvas
from ui.win.maf.hof.dlf.DeckListCanvasFrame import DeckListCanvasFrame
from ui.win.maf.hof.dlf.DeckListScrollbar import DeckListScrollbar
from ui.win.maf.hof.dlf.SubtitleText import SubtitleText

class DeckListFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.canvas = DeckListCanvas(self.window, self)
        self.scrollbar = DeckListScrollbar(self.window, self, self.canvas)
        self.canvas_frame = DeckListCanvasFrame(self.window, self, self.canvas)
        self.canvas.put_frame_in_window(self.canvas_frame, self.scrollbar)
        self.subtitle_text = SubtitleText(self.window, self.canvas_frame)
        self.deck_card_frames = []
        for deck in self.window.database.get_decks():
            self.deck_card_frames.append(DeckCardFrame(self.window, self.canvas_frame, deck))
        self.create_deck_button = CreateDeckButton(self.window, self.canvas_frame)
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))
        for widget in (self.canvas_frame, self.subtitle_text, self.create_deck_button, *self.deck_card_frames):
            widget.bind('<MouseWheel>', self.on_mousewheel)
    
    def on_mousewheel(self, event) -> None:
        self.canvas.yview_scroll(-1 * (event.delta // 120), 'units')