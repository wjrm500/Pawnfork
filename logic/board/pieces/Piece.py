from logic.board.Square import Square
from logic.enums.Colour import Colour

class Piece:
    def __init__(self, colour: Colour, square: Square) -> None:
        self.colour = colour
        self.square = square

    def image_filepath(self) -> str:
        piece_name = self.__class__.__name__.lower()
        return f'./static/images/pieces/unicode/{self.colour.value}/{piece_name}.png'
    
    def move(self, square: Square) -> None:
        self.square = square
        square.piece = self