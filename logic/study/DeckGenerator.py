from time import time
from stockfish import Stockfish
from typing import Dict, List

import logic.consts.filepaths as filepaths
from logic.enums.Color import Color
from logic.study.sqlalchemy.Database import Database
from logic.study.sqlalchemy.Deck import Deck

class DeckGenerator:
    def __init__(self, deck_position_dict: Dict, turn_depth: int, response_depth: int, player_color = Color.WHITE) -> None:
        self.stockfish = Stockfish(filepaths.STOCKFISH)
        self.database = Database()
        self.deck_position_dict = deck_position_dict
        self.turn_depth = turn_depth
        self.response_depth = response_depth
        self.player_color = player_color
    
    def estimate_flashcard_number(self) -> int:
        num_flashcards = sum([self.response_depth ** n for n in range(self.turn_depth)])
        color_to_move = Color.WHITE if len(self.deck_position_dict['moves']) % 2 == 0 else Color.BLACK
        player_to_move = color_to_move.value == self.player_color
        return num_flashcards if player_to_move else num_flashcards * self.response_depth
    
    def generate(self) -> Deck:
        self.deck = self.database.persist_deck(
            self.deck_position_dict,
            self.player_color,
            self.turn_depth,
            self.response_depth
        )
        self.database.commit() # To access the ID
        self.flashcards_generated = 0
        t1 = time()
        print(f'The time at the beginning is: {t1}')
        self.generate_flashcards(self.deck_position_dict['moves'], self.turn_depth)
        t2 = time()
        print(f'The time at the end is: {t2}')
        print(f'Total time taken: {t2 - t1}')
        self.database.commit()
        return self.deck

    def generate_flashcards(self, moves: List[str], turn_depth: int) -> None:
        if turn_depth == 0:
            return
        color_to_move = Color.WHITE if len(moves) % 2 == 0 else Color.BLACK
        player_to_move = color_to_move.value == self.player_color
        self.stockfish.set_position(moves)
        if player_to_move:
            top_moves = self.stockfish.get_top_moves(1)
            top_move = top_moves[0]
            self.database.persist_flashcard(
                self.deck.id,
                moves,
                top_move['Move']
            )
            self.flashcards_generated += 1
            print(f'{self.flashcards_generated} flashcards generated')
            turn_depth -= 1
            new_moves = moves + [top_move['Move']]
            self.generate_flashcards(new_moves, turn_depth)
        else: # Opponent to move
            top_moves = self.stockfish.get_top_moves(self.response_depth)
            centipawns = [x['Centipawn'] for x in top_moves]
            best_centipawn = min(centipawns) if self.player_color == Color.WHITE else max(centipawns) # i.e. Centipawn value of opponent's best move
            filter_good_moves = lambda x: x['Centipawn'] < best_centipawn + 100 if self.player_color == Color.WHITE else lambda x: x['Centipawn'] > best_centipawn - 100
            good_top_moves = filter(filter_good_moves, top_moves) # Filter out any opponent moves that are significantly worse than the best move
            for top_move in good_top_moves:
                new_moves = moves + [top_move['Move']]
                self.generate_flashcards(new_moves, turn_depth)