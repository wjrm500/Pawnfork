from logic.board.Square import Square

class Piece:
    def __init__(self, colour, square: Square) -> None:
        self.colour = colour
        self.square = square

    def image_filepath(self):
        piece_name = self.__class__.__name__.lower()
        return f'./static/images/pieces/originals/{self.colour}/{piece_name}.png'
    
    def move(self, square):
        self.square = square