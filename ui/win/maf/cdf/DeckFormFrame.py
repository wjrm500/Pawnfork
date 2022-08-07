from stockfish import Stockfish
import tkinter as tk

from logic.consts.deck_positions import deck_positions
import logic.consts.filepaths as filepaths
from logic.enums.Colour import Colour
from logic.study.DeckGenerator import DeckGenerator
from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.cdf.dff.ConfirmCancelFrame import ConfirmCancelFrame
from ui.win.maf.cdf.dff.CreateDeckButton import CreateDeckButton
from ui.win.maf.cdf.dff.PostSubmitText import PostSubmitText
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
        self.post_submit_text = PostSubmitText(self.window, self)
        self.post_submit_text.pack_forget()
        self.confirm_cancel_frame = ConfirmCancelFrame(self.window, self)
        self.confirm_cancel_frame.pack_forget()
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))
    
    def show_error(self, text: str) -> None:
        self.post_submit_text.configure(foreground = ColorConsts.ERROR)
        self.post_submit_text.configure(text = text)
        self.post_submit_text.pack()
    
    def instantiate_deck_generator(self, opening: str, turn_depth: int, response_depth: int) -> None:
        self.stockfish = Stockfish(filepaths.STOCKFISH)
        deck_position_dict = next(filter(lambda x: x['name'] == opening, deck_positions.values()))
        self.deck_generator = DeckGenerator(
            deck_position_dict = deck_position_dict,
            turn_depth = turn_depth,
            response_depth = response_depth,
            player_colour = Colour.WHITE # TODO: support black
        )
    
    def show_estimated_flashcard_number(self, estimated_flashcard_number: str) -> None:
        for widget in (
            self.opening_field_frame.field,
            self.turn_depth_field_frame.field,
            self.response_depth_field_frame.field,
            self.create_deck_button
            ):
            widget.configure(state = tk.DISABLED)
        self.post_submit_text.configure(foreground = ColorConsts.BLACK)
        text = f'Up to {estimated_flashcard_number} flashcards may be created'
        self.post_submit_text.configure(text = text)
        self.post_submit_text.pack()
        self.confirm_cancel_frame.pack()
    
    def handle_confirm(self, event) -> None:
        pass

    def handle_cancel(self, event) -> None:
        for widget in (
            self.opening_field_frame.field,
            self.turn_depth_field_frame.field,
            self.response_depth_field_frame.field,
            self.create_deck_button
            ):
            widget.configure(state = tk.NORMAL)
        self.post_submit_text.pack_forget()
        self.confirm_cancel_frame.pack_forget()