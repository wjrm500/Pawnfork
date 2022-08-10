from stockfish import Stockfish

from logic.board.Square import Square
from logic.board.pieces import *
import logic.consts.filepaths as filepaths
from logic.enums.Color import Color
from logic.study.sqlalchemy.Flashcard import Flashcard

class Board:
    def __init__(self, flashcard: Flashcard = None) -> None:
        self.stockfish = Stockfish(path = filepaths.STOCKFISH)
        self.squares = {}
        self.pieces = []
        self.position = []
        for file in range(1, 9):
            for rank in range(1, 9):
                square = Square(file, rank)
                self.add_square(square)
        self.add_pieces()
        if flashcard is not None:
            for move in flashcard.moves:
                self.move_piece(move.definition)
    
    def add_square(self, square: Square) -> None:
        if square.file_name not in self.squares:
            self.squares[square.file_name] = {}
        self.squares[square.file_name][square.rank_name] = square
    
    def get_square(self, square_str):
        file_name, rank_name = list(square_str)
        return self.squares[file_name][rank_name]
    
    def add_piece(self, piece, color, square: Square):
        piece = piece(color, square)
        square.set_piece(piece)
        self.pieces.append(piece)
    
    def add_pieces(self):
        # Add white pieces
        self.add_piece(Pawn, Color.WHITE, self.get_square('a2'))
        self.add_piece(Pawn, Color.WHITE, self.get_square('b2'))
        self.add_piece(Pawn, Color.WHITE, self.get_square('c2'))
        self.add_piece(Pawn, Color.WHITE, self.get_square('d2'))
        self.add_piece(Pawn, Color.WHITE, self.get_square('e2'))
        self.add_piece(Pawn, Color.WHITE, self.get_square('f2'))
        self.add_piece(Pawn, Color.WHITE, self.get_square('g2'))
        self.add_piece(Pawn, Color.WHITE, self.get_square('h2'))
        self.add_piece(Rook, Color.WHITE, self.get_square('a1'))
        self.add_piece(Knight, Color.WHITE, self.get_square('b1'))
        self.add_piece(Bishop, Color.WHITE, self.get_square('c1'))
        self.add_piece(Queen, Color.WHITE, self.get_square('d1'))
        self.add_piece(King, Color.WHITE, self.get_square('e1'))
        self.add_piece(Bishop, Color.WHITE, self.get_square('f1'))
        self.add_piece(Knight, Color.WHITE, self.get_square('g1'))
        self.add_piece(Rook, Color.WHITE, self.get_square('h1'))

        # Add black pieces
        self.add_piece(Pawn, Color.BLACK, self.get_square('a7'))
        self.add_piece(Pawn, Color.BLACK, self.get_square('b7'))
        self.add_piece(Pawn, Color.BLACK, self.get_square('c7'))
        self.add_piece(Pawn, Color.BLACK, self.get_square('d7'))
        self.add_piece(Pawn, Color.BLACK, self.get_square('e7'))
        self.add_piece(Pawn, Color.BLACK, self.get_square('f7'))
        self.add_piece(Pawn, Color.BLACK, self.get_square('g7'))
        self.add_piece(Pawn, Color.BLACK, self.get_square('h7'))
        self.add_piece(Rook, Color.BLACK, self.get_square('a8'))
        self.add_piece(Knight, Color.BLACK, self.get_square('b8'))
        self.add_piece(Bishop, Color.BLACK, self.get_square('c8'))
        self.add_piece(Queen, Color.BLACK, self.get_square('d8'))
        self.add_piece(King, Color.BLACK, self.get_square('e8'))
        self.add_piece(Bishop, Color.BLACK, self.get_square('f8'))
        self.add_piece(Knight, Color.BLACK, self.get_square('g8'))
        self.add_piece(Rook, Color.BLACK, self.get_square('h8'))
    
    def move_piece(self, move_str: str) -> str:
        from_square_str, to_square_str = move_str[:2], move_str[2:]
        from_square = self.get_square(from_square_str)
        moving_piece = from_square.piece
        if not moving_piece:
            raise Exception(f'No piece on square {from_square_str}')
        move_valid = self.stockfish.is_move_correct(move_str)
        if not move_valid:
            raise Exception('Move invalid')
        to_square = self.get_square(to_square_str)

        # Handle capture
        move_capture = self.stockfish.will_move_be_a_capture(move_str)
        if move_capture == Stockfish.Capture.DIRECT_CAPTURE:
            captured_piece = to_square.piece
            captured_piece.captured = True
        elif move_capture == Stockfish.Capture.EN_PASSANT:
            captured_piece_square_rank = 4 if to_square.rank == 3 else 6
            captured_piece_square = self.get_square(f'{to_square.file_name}{captured_piece_square_rank}')
            captured_piece = captured_piece_square.piece
            captured_piece.captured = True

        # Move piece
        moving_piece.move(to_square)

        # Handle castling rook
        if moving_piece.__class__ == King and abs(to_square.file - from_square.file) > 1:
            rook_from_file_name = 'a' if to_square.file_name == 'b' else 'h'
            rook_rank = to_square.rank
            rook_from_square = self.get_square(f'{rook_from_file_name}{rook_rank}')
            rook_to_file = 'c' if to_square.file_name == 'b' else 'f'
            rook_to_square = self.get_square(f'{rook_to_file}{rook_rank}')
            moving_rook = rook_from_square.piece
            moving_rook.move(rook_to_square)

        self.stockfish.make_moves_from_current_position([move_str])
        self.position.append(move_str)