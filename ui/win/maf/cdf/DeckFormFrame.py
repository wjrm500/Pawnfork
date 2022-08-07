from typing import List, Literal
import tkinter as tk

from logic.consts.deck_positions import deck_positions
import logic.consts.filepaths as filepaths
from logic.enums.Colour import Colour
from logic.study.DeckGenerator import DeckGenerator
from ui.consts.ColorConsts import ColorConsts
from ui.win.maf.cdf.dff.ConfirmCancelFrame import ConfirmCancelFrame
from ui.win.maf.cdf.dff.CreateDeckButton import CreateDeckButton
from ui.win.maf.cdf.dff.CreatingText import CreatingText
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
        self.creating_text = CreatingText(self.window, self)
        self.creating_text.pack_forget()
        self.pack(fill = tk.BOTH, expand = True, padx = 20, pady = (0, 20))
    
    def show_error(self, text: str) -> None:
        self.post_submit_text.configure(foreground = ColorConsts.ERROR)
        self.post_submit_text.configure(text = text)
        self.post_submit_text.pack()
    
    def instantiate_deck_generator(self, opening: str, turn_depth: int, response_depth: int) -> None:
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
    
    def handle_create(self, event) -> None:
        opening = self.opening_field_frame.field.option_var.get()
        turn_depth = self.turn_depth_field_frame.field.get()
        response_depth = self.response_depth_field_frame.field.get()
        error_messages = []
        error_messages = self.validate_opening(error_messages, opening)
        error_messages = self.validate_depth(error_messages, turn_depth, 'Turn')
        error_messages = self.validate_depth(error_messages, response_depth, 'Response')
        if len(error_messages):
            error_message = '\n'.join(error_messages)
            self.show_error(error_message)
        else:
            self.instantiate_deck_generator(opening, int(turn_depth), int(response_depth))
            self.show_estimated_flashcard_number(self.deck_generator.estimate_flashcard_number())
    
    def handle_confirm(self, event) -> None:
        self.creating_text.pack()
        self.window.update_idletasks()
        self.deck_generator.generate()
        self.window.main_frame.set_frame_to_home()

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
    
    # Private methods
    
    def validate_opening(self, error_messages: List[str], opening: str) -> str:
        if opening == '':
            error_messages.append('Opening is required')
        return error_messages
    
    def validate_depth(self, error_messages: List[str], depth: int, type: Literal['Turn', 'Response']) -> None:
        if depth == '':
            return error_messages + [f'{type} depth is required']
        if not depth.isnumeric():
            return error_messages + [f'{type} depth must be numeric']
        max_depth = 10
        if int(depth) > max_depth:
            return error_messages + [f'{type} depth cannot exceed {max_depth}']
        return error_messages