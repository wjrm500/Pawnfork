from stockfish import Stockfish
from typing import List

from logic.enums.Colour import Colour
from logic.study.Flashcard import Flashcard
from logic.study.Deck import Deck

class DeckGenerator:
    def __init__(self, start_position: List, turn_depth: int, response_depth: int, player_colour = Colour.WHITE) -> None:
        self.start_position = start_position
        self.turn_depth = turn_depth
        self.response_depth = response_depth
        self.player_colour = player_colour
    
    def estimate_flashcard_number(self) -> int:
        num_flashcards = sum([self.response_depth ** n for n in range(self.turn_depth)])
        colour_to_move = Colour.WHITE if len(self.start_position) % 2 == 0 else Colour.BLACK
        player_to_move = colour_to_move == self.player_colour
        return num_flashcards if player_to_move else num_flashcards * self.response_depth
    
    def generate(self, stockfish: Stockfish) -> Deck:
        self.deck = Deck(self.start_position, self.player_colour)
        self.generate_flashcards(stockfish, self.start_position, self.turn_depth, self.response_depth, self.player_colour)
        return self.deck

    def generate_flashcards(self, stockfish: Stockfish, position: List, turn_depth: int, response_depth: int, player_colour: Colour = Colour.WHITE) -> None:
        if turn_depth == 0:
            return
        colour_to_move = Colour.WHITE if len(position) % 2 == 0 else Colour.BLACK
        player_to_move = colour_to_move == player_colour
        stockfish.set_position(position)
        if player_to_move:
            top_moves = stockfish.get_top_moves(1)
            top_move = top_moves[0]
            flashcard = Flashcard(position, top_move['Move'])
            self.deck.add_flashcard(flashcard)
            turn_depth -= 1
            new_position = position + [top_move['Move']]
            self.generate_flashcards(stockfish, new_position, turn_depth, response_depth, player_colour)
        else: # Opponent to move
            top_moves = stockfish.get_top_moves(response_depth)
            centipawns = [x['Centipawn'] for x in top_moves]
            best_centipawn = min(centipawns) if player_colour == Colour.WHITE else max(centipawns) # i.e. Centipawn value of opponent's best move
            filter_good_moves = lambda x: x['Centipawn'] < best_centipawn + 100 if player_colour == Colour.WHITE else lambda x: x['Centipawn'] > best_centipawn - 100
            good_top_moves = filter(filter_good_moves, top_moves) # Filter out any opponent moves that are significantly worse than the best move
            for top_move in good_top_moves:
                new_position = position + [top_move['Move']]
                self.generate_flashcards(stockfish, new_position, turn_depth, response_depth, player_colour)