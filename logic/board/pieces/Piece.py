from logic.board.Square import Square
from logic.enums.Color import Color
import ui.consts.filepaths as ui_filepaths

class Piece:
    def __init__(self, color: Color, square: Square) -> None:
        self.color = color
        self.square = square
        self.captured = False

    def image_filepath(self) -> str:
        piece_name = self.__class__.__name__.lower()
        return ui_filepaths.PIECE_IMAGE.format(color = self.color.value, piece_name = piece_name)
    
    def move(self, square: Square) -> None:
        self.square = square
        square.piece = self