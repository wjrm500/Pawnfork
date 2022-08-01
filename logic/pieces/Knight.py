from logic.pieces.Piece import Piece
from logic.Square import Square

class Knight(Piece):
    def __init__(self, colour, square: Square) -> None:
        super().__init__(colour, square)