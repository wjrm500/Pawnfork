import tkinter as tk
from tkinter import ttk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.hof.dlf.CreateDeckButton import CreateDeckButton
from ui.win.maf.hof.dlf.DeckCardFrame import DeckCardFrame
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
        self.canvas = tk.Canvas(self, bd = 0, highlightthickness = 0, background = ColorConsts.WHITE)
        scrollbar = ttk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.canvas.pack(side = tk.LEFT, expand = True, fill = 'both')
        scrollbar.pack(side = tk.RIGHT, fill = 'y')
        self.scrollable_frame = tk.Frame(self.canvas, background = ColorConsts.WHITE)
        self.scrollable_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox('all')))
        self.canvas_frame = self.canvas.create_window((0, 0), window = self.scrollable_frame, anchor = tk.NW, width = self.window.dimension - 50)
        self.canvas.configure(yscrollcommand = scrollbar.set)
        self.subtitle_text = SubtitleText(self.window, self.scrollable_frame)
        self.deck_card_frames = []
        for deck in self.window.database.get_decks():
            self.deck_card_frames.append(DeckCardFrame(self.window, self.scrollable_frame, deck))
        self.create_deck_button = CreateDeckButton(self.window, self.scrollable_frame)
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))
        self.canvas.update_idletasks()
        print(self.canvas.winfo_reqwidth())
        for widget in (self.scrollable_frame, self.subtitle_text, self.create_deck_button, *self.deck_card_frames):
            widget.bind('<MouseWheel>', self.on_mousewheel)
    
    def on_mousewheel(self, event) -> None:
        self.canvas.yview_scroll(-1 * (event.delta // 120), 'units')