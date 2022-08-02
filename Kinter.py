from PIL import ImageTk, Image
import tkinter
from typing import List

from logic.pieces import *

class Kinter():
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title('Pawnfork')
        self.frame = tkinter.Frame(self.root)
        self.frame.pack()
        self.canvas_dimension = 1000
        self.canvas = tkinter.Canvas(self.frame, height = self.canvas_dimension, width = self.canvas_dimension)
        self.canvas.pack()
        self.background = tkinter.PhotoImage(file = './static/images/chessboard.png')
        self.canvas.create_image(0, 0, anchor = tkinter.NW, image = self.background)
        self.images = []

    def add_pieces(self, pieces: List[Piece]) -> None:
        for piece in pieces:
            virtual_x, virtual_y = piece.square.centre
            real_x, real_y = virtual_x * self.canvas_dimension / 8, virtual_y * self.canvas_dimension / 8
            print(real_x, real_y)
            image = Image.open(piece.image_filepath())
            image_dimension_dict = {
                Bishop: 15,
                King: 10,
                Knight: 16,
                Pawn: 20,
                Queen: 10,
                Rook: 18
            }
            image_dimension = int(self.canvas_dimension / image_dimension_dict[piece.__class__])
            image = image.resize((image_dimension, image_dimension))
            image = ImageTk.PhotoImage(image)
            self.images.append(image)
            self.canvas.create_image(real_x, real_y, anchor = tkinter.CENTER, image = image)
    
    def run(self) -> None:
        self.root.mainloop()