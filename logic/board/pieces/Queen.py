from logic.board.pieces.Piece import Piece
from logic.board.Square import Square

class Queen(Piece):
    def __init__(self, color, square: Square) -> None:
        super().__init__(color, square)