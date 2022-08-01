from logic.Board import Board
from logic.Square import Square
from Kinter import Kinter

board = Board()
squares = []
for file in range(1, 9):
    for rank in range(1, 9):
        square = Square(file, rank)
        board.add_square(square)
    
board.add_pieces()

kinter = Kinter()
kinter.add_pieces(board.pieces)
kinter.run()