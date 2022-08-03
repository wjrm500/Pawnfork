from typing import List

import logic.consts.positions as positions
from logic.consts.positions import Position
from logic.enums.Colour import Colour
from logic.study.Flashcard import Flashcard

class Deck:
    def __init__(self, start_position: Position, player_colour: Colour) -> None:
        self.start_position = start_position
        self.player_colour = player_colour
        self.flashcards = []
    
    def __iter__(self):
        yield from self.flashcards
    
    def add_flashcard(self, flashcard: Flashcard) -> None:
        self.flashcards.append(flashcard)
    
    # def persist(self) -> None:

    
    @staticmethod
    def load(db) -> 'Deck':
        pass