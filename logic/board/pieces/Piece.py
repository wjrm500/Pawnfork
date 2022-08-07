from logic.board.Square import Square
from logic.enums.Colour import Colour
import ui.consts.filepaths as ui_filepaths

class Piece:
    def __init__(self, colour: Colour, square: Square) -> None:
        self.colour = colour
        self.square = square

    def image_filepath(self) -> str:
        piece_name = self.__class__.__name__.lower()
        return ui_filepaths.PIECE_IMAGE.format(color = self.colour.value, piece_name = piece_name)
    
    def move(self, square: Square) -> None:
        self.square = square
        square.piece = self