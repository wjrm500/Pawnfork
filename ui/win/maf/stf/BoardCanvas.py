from PIL import ImageTk, Image
import tkinter as tk
from typing import List

from logic.board.pieces import *
from ui.ColorConsts import ColorConsts

class BoardCanvas(tk.Canvas):
    def __init__(self, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.BACKGROUND_COLOR
        )
        self.dimension = 500
        self.config(height = self.dimension, width = self.dimension)
        self.images = []
        self.add_background()
        self.pack()
    
    def add_background(self) -> None:
        image = Image.open('./static/images/chessboard.png')
        image = image.resize((self.dimension, self.dimension), Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(image)
        self.create_image(0, 0, anchor = tk.NW, image = self.background)

    def add_pieces(self, pieces: List[Piece]) -> None:
        for piece in pieces:
            virtual_x, virtual_y = piece.square.centre
            real_x, real_y = virtual_x * self.dimension / 8, virtual_y * self.dimension / 8
            image = Image.open(piece.image_filepath())
            image_dimension_dict = {
                Bishop: 15,
                King: 10,
                Knight: 16,
                Pawn: 20,
                Queen: 10,
                Rook: 18
            }
            image_dimension = int(self.dimension / image_dimension_dict[piece.__class__])
            image = image.resize((image_dimension, image_dimension))
            image = ImageTk.PhotoImage(image)
            self.images.append(image)
            self.create_image(real_x, real_y, anchor = tk.CENTER, image = image)