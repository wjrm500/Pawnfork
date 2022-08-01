from logic.Square import Square
from logic.pieces import *
import logic.consts.colours as colours

class Board:
    def __init__(self) -> None:
        self.squares = {}
        self.pieces = []
    
    def add_square(self, square: Square) -> None:
        if square.file_name not in self.squares:
            self.squares[square.file_name] = {}
        self.squares[square.file_name][square.rank_name] = square
    
    def get_square(self, square_string):
        file_name, rank_name = list(square_string)
        return self.squares[file_name][rank_name]
    
    def add_piece(self, piece, colour, square: Square):
        piece = piece(colour, square)
        square.set_piece(piece)
        self.pieces.append(piece)
    
    def add_pieces(self):
        # Add white pieces
        self.add_piece(Pawn, colours.WHITE, self.get_square('a2'))
        self.add_piece(Pawn, colours.WHITE, self.get_square('b2'))
        self.add_piece(Pawn, colours.WHITE, self.get_square('c2'))
        self.add_piece(Pawn, colours.WHITE, self.get_square('d2'))
        self.add_piece(Pawn, colours.WHITE, self.get_square('e2'))
        self.add_piece(Pawn, colours.WHITE, self.get_square('f2'))
        self.add_piece(Pawn, colours.WHITE, self.get_square('g2'))
        self.add_piece(Pawn, colours.WHITE, self.get_square('h2'))
        self.add_piece(Rook, colours.WHITE, self.get_square('a1'))
        self.add_piece(Knight, colours.WHITE, self.get_square('b1'))
        self.add_piece(Bishop, colours.WHITE, self.get_square('c1'))
        self.add_piece(Queen, colours.WHITE, self.get_square('d1'))
        self.add_piece(King, colours.WHITE, self.get_square('e1'))
        self.add_piece(Bishop, colours.WHITE, self.get_square('f1'))
        self.add_piece(Knight, colours.WHITE, self.get_square('g1'))
        self.add_piece(Rook, colours.WHITE, self.get_square('h1'))

        # Add black pieces
        self.add_piece(Pawn, colours.BLACK, self.get_square('a7'))
        self.add_piece(Pawn, colours.BLACK, self.get_square('b7'))
        self.add_piece(Pawn, colours.BLACK, self.get_square('c7'))
        self.add_piece(Pawn, colours.BLACK, self.get_square('d7'))
        self.add_piece(Pawn, colours.BLACK, self.get_square('e7'))
        self.add_piece(Pawn, colours.BLACK, self.get_square('f7'))
        self.add_piece(Pawn, colours.BLACK, self.get_square('g7'))
        self.add_piece(Pawn, colours.BLACK, self.get_square('h7'))
        self.add_piece(Rook, colours.BLACK, self.get_square('a8'))
        self.add_piece(Knight, colours.BLACK, self.get_square('b8'))
        self.add_piece(Bishop, colours.BLACK, self.get_square('c8'))
        self.add_piece(Queen, colours.BLACK, self.get_square('d8'))
        self.add_piece(King, colours.BLACK, self.get_square('e8'))
        self.add_piece(Bishop, colours.BLACK, self.get_square('f8'))
        self.add_piece(Knight, colours.BLACK, self.get_square('g8'))
        self.add_piece(Rook, colours.BLACK, self.get_square('h8'))