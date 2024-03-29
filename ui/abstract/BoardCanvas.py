import math
from stockfish import Stockfish
import string
from PIL import ImageTk, Image
import tkinter as tk
from typing import List

from logic.board.pieces import *
from logic.enums.Color import Color
from ui.consts.ColorConsts import ColorConsts
import ui.consts.filepaths as ui_filepaths

class BoardCanvas(tk.Canvas):
    def __init__(self, window: tk.Tk, master: tk.Widget, color: Color) -> None:
        super().__init__(
            master,
            background = ColorConsts.MEDIUM_GREY
        )
        self.window = window
        self.color = Color(color)
        self.dimension = 500
        self.config(height = self.dimension, width = self.dimension)
        self.piece_image_dimension = int(self.dimension / 6)
        self.images = []
        self.add_background()
        self.pack()
    
    def add_background(self) -> None:
        image = Image.open(ui_filepaths.CHESSBOARD_IMAGE)
        image = image.resize((self.dimension, self.dimension), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)
        self.create_image(0, 0, anchor = tk.NW, image = self.background_image)

    def add_pieces(self, pieces: List[Piece]) -> None:
        self.piece_elements = []
        for piece in pieces:
            if piece.captured:
                continue
            virtual_x, virtual_y = piece.square.centre
            real_x, real_y = virtual_x * self.dimension / 8, virtual_y * self.dimension / 8
            if self.color == Color.BLACK:
                real_x, real_y = self.dimension - real_x, self.dimension - real_y
            real_y += self.dimension / 75 # This accounts for the fact that for some reason pieces in images are not centered
            image = Image.open(piece.image_filepath())
            image = image.resize((self.piece_image_dimension, self.piece_image_dimension))
            image = ImageTk.PhotoImage(image)
            self.images.append(image)
            piece_element = self.create_image(real_x, real_y, anchor = tk.CENTER, image = image)
            self.addtag_withtag(f'type_{piece.__class__.__name__}', piece_element)
            self.addtag_withtag(f'square_{str(piece.square)}', piece_element)
            self.piece_elements.append(piece_element)
        for piece_element in self.piece_elements:
            self.tag_bind(piece_element, '<Button-1>', self.piece_mousedown_handler)
            self.tag_bind(piece_element, '<ButtonRelease-1>', self.piece_mouseup_handler)
    
    def piece_mousedown_handler(self, event) -> None:
        self.moving_element = self.find_closest(event.x, event.y)
        self.bind('<Motion>', lambda e: self.moveto(self.moving_element, e.x - (self.piece_image_dimension / 2), e.y - (self.piece_image_dimension / 2)))
    
    def piece_mouseup_handler(self, event) -> None:
        self.unbind('<Motion>')
        real_x, real_y = event.x, event.y
        if self.color == Color.BLACK:
            real_x, real_y = self.dimension - real_x, self.dimension - real_y
        virtual_x, virtual_y = real_x / self.dimension * 8, real_y / self.dimension * 8
        from_square = next(filter(lambda tag: tag.startswith('square_'), self.gettags(self.moving_element))).split('_')[1]
        to_square = self.get_square_from_virtual_coords(virtual_x, virtual_y)
        move = f'{from_square}{to_square}'
        move_valid = self.master.board.stockfish.is_move_correct(move)
        to_square = to_square if move_valid else from_square
        self.move_piece(from_square, to_square)
    
    def get_square_from_virtual_coords(self, virtual_x: int, virtual_y: int) -> None:
        file_name = string.ascii_lowercase[math.floor(virtual_x)]
        rank_name = list(reversed(range(1, 9)))[math.floor(virtual_y)]
        return f'{file_name}{rank_name}'
    
    def move_piece(self, from_square: str, to_square: str, castle_castling: bool = False) -> None:
        pass
        move = f'{from_square}{to_square}'

        # Handle basic movement
        virtual_x = string.ascii_lowercase.index(to_square[0]) + 0.5
        virtual_y = list(reversed(range(1, 9)))[int(to_square[1]) - 1] - 0.5
        real_x, real_y = virtual_x * self.dimension / 8, virtual_y * self.dimension / 8
        if self.color == Color.BLACK:
            real_x, real_y = self.dimension - real_x, self.dimension - real_y
        real_x, real_y = real_x - (self.piece_image_dimension / 2), real_y - (self.piece_image_dimension / 2)
        real_y += self.dimension / 75
        self.moveto(self.moving_element, real_x, real_y)

        # Handle capture
        move_capture = self.master.board.stockfish.will_move_be_a_capture(move) # Anything but Stockfish.Capture.NO_CAPTURE
        if move_capture == Stockfish.Capture.DIRECT_CAPTURE:
            captured_piece_element = self.find_withtag(f'square_{to_square}')
            self.delete(captured_piece_element)
        elif move_capture == Stockfish.Capture.EN_PASSANT:
            captured_piece_square_rank = 4 if int(to_square[1]) == 3 else 6
            captured_piece_square = f'{to_square[0]}{captured_piece_square_rank}'
            captured_piece_element = self.find_withtag(f'square_{captured_piece_square}')
            self.delete(captured_piece_element)
        
        # Update moving element canvas object metadata
        old_tags = self.gettags(self.moving_element)
        new_tags = tuple((f'square_{to_square}' if tag.startswith('square_') else tag) for tag in old_tags)
        self.itemconfig(self.moving_element, tags = new_tags)
        
        if not castle_castling:
            castling_move = 'type_King' in self.gettags(self.moving_element) and abs(ord(from_square[0]) - ord(to_square[0])) > 1
            if castling_move:
                # Handle castling rook
                rook_from_file = 'a' if to_square[0] == 'b' else 'h'
                rook_rank = to_square[1]
                rook_from_square = f'{rook_from_file}{rook_rank}'
                rook_to_file = 'c' if to_square[0] == 'b' else 'f'
                rook_to_square = f'{rook_to_file}{rook_rank}'
                self.moving_element = self.find_withtag(f'square_{rook_from_square}')
                self.move_piece(rook_from_square, rook_to_square, castle_castling = True)

            # Update backend
            self.master.move_piece(move)