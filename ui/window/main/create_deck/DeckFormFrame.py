import math
from typing import List, Literal
import tkinter as tk

from logic.consts.openings import openings
from logic.enums.Color import Color
from logic.study.DeckGenerator import DeckGenerator
from ui.consts.ColorConsts import ColorConsts
from ui.window.main.create_deck.deck_form.ConfirmCancelFrame import ConfirmCancelFrame
from ui.window.main.create_deck.deck_form.CreateDeckButton import CreateDeckButton
from ui.window.main.create_deck.deck_form.CreatingText import CreatingText
from ui.window.main.create_deck.deck_form.PostSubmitText import PostSubmitText
from ui.window.main.create_deck.deck_form.form_field.CreateOpeningButton import CreateOpeningButton
from ui.window.main.create_deck.deck_form.form_field.OpeningEntry import OpeningEntry
from ui.window.main.create_deck.deck_form.form_field.OpeningLabel import OpeningLabel
from ui.window.main.create_deck.deck_form.form_field.PlayerColorEntry import PlayerColorEntry
from ui.window.main.create_deck.deck_form.form_field.PlayerColorLabel import PlayerColorLabel
from ui.window.main.create_deck.deck_form.form_field.ResponseDepthEntry import ResponseDepthEntry
from ui.window.main.create_deck.deck_form.form_field.ResponseDepthLabel import ResponseDepthLabel
from ui.window.main.create_deck.deck_form.form_field.TurnDepthEntry import TurnDepthEntry
from ui.window.main.create_deck.deck_form.form_field.TurnDepthLabel import TurnDepthLabel
from ui.window.main.create_deck.deck_form.FormFieldFrame import FormFieldFrame
from ui.window.main.create_deck.deck_form.SubtitleText import SubtitleText
from ui.window.main.create_deck.deck_form.form_field.OpeningVar import OpeningVar
from ui.window.main.create_deck.deck_form.form_field.PlayerColorVar import PlayerColorVar

class DeckFormFrame(tk.Frame):
    def __init__(self, window: tk.Tk, master: tk.Widget):
        super().__init__(
            master,
            background = ColorConsts.WHITE,
            highlightbackground = ColorConsts.BLACK,
            highlightthickness = 2
        )
        self.window = window
        self.subtitle_text = SubtitleText(self.window, self)
        self.opening_field_frame = FormFieldFrame(self.window, self, OpeningLabel, OpeningEntry, OpeningVar, CreateOpeningButton)
        self.player_color_field_frame = FormFieldFrame(self.window, self, PlayerColorLabel, PlayerColorEntry, PlayerColorVar)
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
    
    def instantiate_deck_generator(self, opening_name: str, player_color: Color, turn_depth: int, response_depth: int) -> None:
        opening = self.window.database.get_opening_by_name(opening_name)
        self.deck_generator = DeckGenerator(
            opening = opening,
            turn_depth = turn_depth,
            response_depth = response_depth,
            player_color = player_color
        )
    
    def handle_successful_form_submit(self) -> None:
        estimated_flashcards = self.deck_generator.estimate_flashcard_number()
        for widget in (
            self.opening_field_frame.field,
            self.player_color_field_frame.field,
            self.turn_depth_field_frame.field,
            self.response_depth_field_frame.field,
            self.create_deck_button
            ):
            widget.configure(state = tk.DISABLED)
        self.post_submit_text.show_estimated_flashcards(estimated_flashcards)
        self.confirm_cancel_frame.pack()
    
    def handle_create(self) -> None:
        opening_name = self.opening_field_frame.field.option_var.get()
        player_color = self.player_color_field_frame.option_var.get()
        turn_depth = self.turn_depth_field_frame.field.get()
        response_depth = self.response_depth_field_frame.field.get()
        error_messages = []
        error_messages = self.validate_opening(error_messages, opening_name)
        error_messages = self.validate_player_color(error_messages, player_color)
        error_messages = self.validate_depth(error_messages, turn_depth, 'Turn depth')
        error_messages = self.validate_depth(error_messages, response_depth, 'Response depth')
        if len(error_messages):
            error_message = '\n'.join(error_messages)
            self.post_submit_text.show_error(error_message)
        else:
            existing_decks = self.window.database.get_decks()
            for existing_deck in existing_decks:
                if opening_name == existing_deck.opening.name \
                    and player_color == existing_deck.player_color \
                    and int(turn_depth) == existing_deck.turn_depth \
                    and int(response_depth) == existing_deck.response_depth:
                    self.post_submit_text.show_error(PostSubmitText.ERROR_DECK_EXISTS)
                    break
            else:
                self.instantiate_deck_generator(opening_name, player_color, int(turn_depth), int(response_depth))
                self.handle_successful_form_submit()
    
    def handle_confirm(self) -> None:
        self.creating_text.pack()
        self.window.update_idletasks()
        self.deck_generator.generate()
        self.window.main_frame.set_frame_to_home()

    def handle_cancel(self) -> None:
        for widget in (
            self.opening_field_frame.field,
            self.player_color_field_frame.field,
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
    
    def validate_player_color(self, error_messages: List[str], player_color: Color) -> None:
        if player_color == '':
            error_messages.append('Player colour is required')
        return error_messages
    
    def validate_depth(self, error_messages: List[str], depth: int, depth_type: Literal['Turn depth', 'Response depth']) -> None:
        if depth == '':
            return error_messages + [PostSubmitText.ERROR_FIELD_REQUIRED.format(depth_type)]
        if not depth.isnumeric():
            return error_messages + [PostSubmitText.ERROR_NOT_NUMERIC.format(depth_type)]
        max_depth = 10
        if int(depth) > max_depth:
            return error_messages + [PostSubmitText.ERROR_MAX_EXCEEDED.format(depth_type, max_depth)]
        return error_messages