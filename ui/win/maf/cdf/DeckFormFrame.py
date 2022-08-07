import tkinter as tk

from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.cdf.dff.CreateDeckButton import CreateDeckButton
from ui.win.maf.cdf.dff.fff.OpeningEntry import OpeningEntry
from ui.win.maf.cdf.dff.fff.OpeningLabel import OpeningLabel
from ui.win.maf.cdf.dff.fff.ResponseDepthEntry import ResponseDepthEntry
from ui.win.maf.cdf.dff.fff.ResponseDepthLabel import ResponseDepthLabel
from ui.win.maf.cdf.dff.fff.TurnDepthEntry import TurnDepthEntry
from ui.win.maf.cdf.dff.fff.TurnDepthLabel import TurnDepthLabel
from ui.win.maf.cdf.dff.FormFieldFrame import FormFieldFrame
from ui.win.maf.cdf.dff.SubtitleText import SubtitleText

class DeckFormFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Frame):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.subtitle_text = SubtitleText(self.window, self)
        self.opening_field_frame = FormFieldFrame(self.window, self, OpeningLabel, OpeningEntry)
        self.turn_depth_field_frame = FormFieldFrame(self.window, self, TurnDepthLabel, TurnDepthEntry)
        self.response_depth_field_frame = FormFieldFrame(self.window, self, ResponseDepthLabel, ResponseDepthEntry)
        self.create_deck_button = CreateDeckButton(self.window, self)
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))