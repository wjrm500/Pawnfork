from logic.board.pieces.Piece import Piece
from logic.board.Square import Square

class King(Piece):
    letter = 'K'

    def __init__(self, color, square: Square) -> None:
        super().__init__(color, square)