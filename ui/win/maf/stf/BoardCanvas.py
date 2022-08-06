from PIL import ImageTk, Image
import tkinter as tk
from typing import List

from logic.board.pieces import *
from ui.ColorConsts import ColorConsts

class BoardCanvas(tk.Canvas):
    def __init__(self, window: tk.Tk, master: tk.Frame) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.dimension = 500
        self.config(height = self.dimension, width = self.dimension)
        self.piece_image_dimension = int(self.dimension / 6)
        self.images = []
        self.add_background()
        self.pack()
    
    def add_background(self) -> None:
        image = Image.open('./static/images/chessboard.png')
        image = image.resize((self.dimension, self.dimension), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)
        self.create_image(0, 0, anchor = tk.NW, image = self.background_image)

    def add_pieces(self, pieces: List[Piece]) -> None:
        self.piece_elements = []
        for piece in pieces:
            virtual_x, virtual_y = piece.square.centre
            real_x, real_y = virtual_x * self.dimension / 8, virtual_y * self.dimension / 8
            real_y += self.dimension / 75 # This accounts for the fact that for some reason pieces in images are not centered
            image = Image.open(piece.image_filepath())
            image = image.resize((self.piece_image_dimension, self.piece_image_dimension))
            image = ImageTk.PhotoImage(image)
            self.images.append(image)
            piece_element = self.create_image(real_x, real_y, anchor = tk.CENTER, image = image)
            self.addtag_withtag(f'type_{piece.__class__.__name__}', piece_element)
            self.piece_elements.append(piece_element)
        for piece_element in self.piece_elements:
            self.tag_bind(piece_element, '<Button-1>', self.piece_mousedown_handler)
            self.tag_bind(piece_element, '<ButtonRelease-1>', lambda e: self.unbind('<Motion>'))
    
    def piece_mousedown_handler(self, event) -> None:
        piece_type = next(filter(lambda x: x.startswith('type_'), self.gettags(self.find_closest(event.x, event.y)))).split('_')[1]
        element_to_move = self.find_closest(event.x, event.y)
        self.bind('<Motion>', lambda e: self.moveto(element_to_move, e.x - (self.piece_image_dimension / 2), e.y - (self.piece_image_dimension / 2)))