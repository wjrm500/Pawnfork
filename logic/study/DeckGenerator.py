from time import time
from stockfish import Stockfish
from typing import List

from ..board.pieces.Pawn import Pawn
from ..board.pieces.King import King

import logic.consts.filepaths as filepaths
from logic.enums.Color import Color
from logic.study.sqlalchemy.Database import Database
from logic.study.sqlalchemy.Deck import Deck
from logic.study.sqlalchemy.Opening import Opening

class DeckGenerator:
    def __init__(self, opening: Opening, turn_depth: int, response_depth: int, player_color = Color.WHITE) -> None:
        self.stockfish = Stockfish(filepaths.STOCKFISH)
        self.database = Database()
        self.opening = opening
        self.turn_depth = turn_depth
        self.response_depth = response_depth
        self.player_color = player_color
    
    def estimate_flashcard_number(self) -> int:
        num_flashcards = sum([self.response_depth ** n for n in range(self.turn_depth)])
        color_to_move = Color.WHITE if len(self.opening.moves) % 2 == 0 else Color.BLACK
        player_to_move = color_to_move.value == self.player_color
        return num_flashcards if player_to_move else num_flashcards * self.response_depth
    
    def generate(self) -> Deck:
        self.deck = self.database.persist_deck(
            self.opening.id,
            self.player_color,
            self.turn_depth,
            self.response_depth
        )
        self.database.commit() # To access the ID
        self.flashcards_generated = 0
        t1 = time()
        print(f'The time at the beginning is: {t1}')
        opening_moves = [move.definition for move in self.opening.moves]
        algebraic_opening_moves = self.get_algebraic_moves_for_opening(opening_moves)
        self.generate_flashcards(opening_moves, algebraic_opening_moves, self.turn_depth)
        t2 = time()
        print(f'The time at the end is: {t2}')
        print(f'Total time taken: {t2 - t1}')
        self.database.commit()
        return self.deck

    def generate_flashcards(self, moves: List[str], algebraic_moves: List[str], turn_depth: int) -> None:
        if turn_depth == 0:
            return
        color_to_move = Color.WHITE if len(moves) % 2 == 0 else Color.BLACK
        player_to_move = color_to_move.value == self.player_color
        self.stockfish.set_position(moves)
        if player_to_move:
            top_moves = self.stockfish.get_top_moves(1)
            top_move = top_moves[0]
            algebraic_move = self.get_algebraic_move(top_move['Move'])
            self.database.persist_flashcard(
                self.deck.id,
                moves,
                algebraic_moves,
                top_move['Move'],
                algebraic_move,
                self.get_algebraic_opponents_move(moves)
            )
            self.flashcards_generated += 1
            print(f'{self.flashcards_generated} flashcards generated')
            turn_depth -= 1
            new_moves = moves + [top_move['Move']]
            new_algebraic_moves = algebraic_moves + [algebraic_move]
            self.generate_flashcards(new_moves, new_algebraic_moves, turn_depth)
        else: # Opponent to move
            top_moves = self.stockfish.get_top_moves(self.response_depth)
            centipawns = [x['Centipawn'] for x in top_moves]
            best_centipawn = min(centipawns) if self.player_color == Color.WHITE else max(centipawns) # i.e. Centipawn value of opponent's best move
            filter_good_moves = lambda x: x['Centipawn'] < best_centipawn + 100 if self.player_color == Color.WHITE else lambda x: x['Centipawn'] > best_centipawn - 100
            good_top_moves = filter(filter_good_moves, top_moves) # Filter out any opponent moves that are significantly worse than the best move
            for top_move in good_top_moves:
                new_moves = moves + [top_move['Move']]
                algebraic_move = self.get_algebraic_opponents_move(new_moves)
                new_algebraic_moves = algebraic_moves + [algebraic_move]
                self.generate_flashcards(new_moves, new_algebraic_moves, turn_depth)
            
    def get_algebraic_move(self, move: str) -> str:
        move_capture = self.stockfish.will_move_be_a_capture(move)
        moving_piece_letter = self.stockfish.get_what_is_on_square(move[:2]).value.upper()
        moving_piece_is_pawn = moving_piece_letter == Pawn.letter
        moving_piece_letter = '' if moving_piece_is_pawn else moving_piece_letter
        # Handle castling
        if moving_piece_letter == King.letter:
            start_file, end_file = move[0], move[2]
            file_shift = abs(ord(start_file) - ord(end_file))
            if file_shift == 2:
                return 'O-O'
            elif file_shift == 3:
                return 'O-O-O'
        # Handle capture
        if move_capture == Stockfish.Capture.DIRECT_CAPTURE:
            if moving_piece_is_pawn:
                return move[:1] + 'x' + move[2:]
            return moving_piece_letter + 'x' + move[2:]
        elif move_capture == Stockfish.Capture.EN_PASSANT:
            return moving_piece_letter + 'x' + move[2:] + ' e.p.'
        else:
            return moving_piece_letter + move[2:]
    
    def get_algebraic_opponents_move(self, moves: List[str]) -> str:
        self.stockfish.set_position(moves[:-1]) # We're only temporarily resetting Stockfish to the previous position in order to check whether the move was a capture
        opponents_move = moves[-1]
        algebraic_opponents_move = self.get_algebraic_move(opponents_move)
        self.stockfish.set_position(moves) # Resetting Stockfish to current position (see note above)
        return algebraic_opponents_move

    def get_algebraic_moves_for_opening(self, moves: List[str]) -> List[str]:
        algebraic_moves = []
        for i in range(len(moves)):
            self.stockfish.set_position(moves[:i])
            algebraic_move = self.get_algebraic_move(moves[i])
            algebraic_moves.append(algebraic_move)
        return algebraic_moves