from logic.Board import Board
from logic.Square import Square
from Kinter import Kinter
from stockfish import Stockfish

board = Board()
squares = []
for file in range(1, 9):
    for rank in range(1, 9):
        square = Square(file, rank)
        board.add_square(square)
    
board.add_pieces()

ITALIAN_GAME = ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4']
for move in ITALIAN_GAME:
    from_square_str, to_square_str = move[:2], move[2:]
    board.get_square(from_square_str).piece.move(board.get_square(to_square_str))

kinter = Kinter()
kinter.add_pieces(board.pieces)
kinter.run()
